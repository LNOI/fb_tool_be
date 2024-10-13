from http.client import HTTPException
from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.domain.model.user_model import UserModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import user_usecase

router = APIRouter()


@router.delete("/{user_id}", response_model=ResponseModel)
async def delete_user(user_id: UUID):
    is_deleted = await user_usecase.delete_user(user_id)
    if not is_deleted:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND, data=False)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=True)
