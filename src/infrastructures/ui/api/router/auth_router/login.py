from black import datetime
from fastapi import APIRouter, Depends, HTTPException, Request,Security
from uuid import UUID


from starlette import status
from typing import Dict
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from src.application.dto.user_dto.user_request_dto import CreateUserRequestDto
from src.domain.model.user_model import UserModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from sqlmodel import select
from src.infrastructures.ui.api.common.utils.redis_util import set_cache, get_cache
from src.middleware import user_usecase

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
import requests

GOOGLE_TOKEN_VALIDATION_URL = "https://www.googleapis.com/oauth2/v1/tokeninfo"

async def validate_access_token(token:str):
    response = requests.get(f"{GOOGLE_TOKEN_VALIDATION_URL}?access_token={token}")
    return response

# async def check_scopes(user_scope: list[str], scope: str):
#     if scope not in user_scope:
#

# mainrole:subrole:read write update delete
# user root
credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
)

async def validate_user(security_scopes: SecurityScopes, request: Request, token: str = Depends(oauth2_scheme)):
    if "user_id" in request.path_params:
        v = get_cache(f"user:{request.path_params.get('user_id')}")
        user = None
        if v is None:
            response = await validate_access_token(token)
            if response.status_code != 200:
                raise credentials_exception
            resp = response.json()

            user = await user_usecase.get_user(user_id=request.path_params.get('user_id'))
            if user is None:
                raise credentials_exception
            data = {
                "access_token": token,
                "user" : {
                    "scopes" : user.scopes,
                }
            }
            set_cache(f"user:{request.path_params.get('user_id')}", data,resp["expires_in"])

        if any([scope in security_scopes.scopes for scope in user.scopes]):
                return None
    else:
        response = await validate_access_token(token)
        if response.status_code != 200:
            raise credentials_exception
        email = request.query_params.get("email")
        query = select(UserModel).where(UserModel.email == email)
        user : UserModel = await user_usecase.query_user(query)
        if user is None:
            raise credentials_exception
        if "admin" in user.scopes:
            return None
    raise credentials_exception

async def get_current_user(token: str = Depends(oauth2_scheme)):
    response = await validate_access_token(token)
    if response.status_code != 200:
        raise credentials_exception
    data = response.json()
    data["access_token"] = token
    return data


@router.post("/first_login", response_model=ResponseModel)
async def first_login(user: CreateUserRequestDto, current_user: Dict = Depends(get_current_user)):
    if current_user["email"] != user.email:
        return CustomJSONResponse(status_code=status.HTTP_401_UNAUTHORIZED)

    user_exists = await user_usecase.get_user(user_id=user.id)
    data = {
        "access_token": current_user["access_token"],
        "user": {
            "scopes": []
        }
    }
    if user_exists:
        data["user"]["scopes"] = user_exists.scopes
        set_cache(f"user:{user.id}", data,ex=current_user["expires_in"])
        return CustomJSONResponse(
            status_code=status.HTTP_200_OK,
            message="User already exists"
        )
    item: UserModel = UserModel(**user.model_dump())
    result = await user_usecase.create_user(item)
    data["user"]["scopes"] = result.scopes
    set_cache(f"user:{user.id}", data, ex=current_user["expires_in"])
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
