from fastapi import APIRouter
from starlette import status

from src.application.dto.user_dto.user_request_dto import CreateUserRequestDto
from src.domain.model.user_model import UserModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import user_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_user(user: CreateUserRequestDto):
    item: UserModel = UserModel(**user.model_dump())
    result = await user_usecase.create_user(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
