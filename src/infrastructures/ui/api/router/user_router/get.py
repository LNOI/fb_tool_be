from uuid import UUID
from fastapi import APIRouter
from select import select
from starlette import status

from src.domain.model.user_model import UserModel
from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import user_usecase

router = APIRouter()

@router.get('/{user_id}', response_model=ResponseModel)
async def get_user(user_id: UUID):
    user = await user_usecase.get_user(user_id)
    if not user:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    return CustomJSONResponse(
        status_code=status.HTTP_200_OK,
        data=user
    )
