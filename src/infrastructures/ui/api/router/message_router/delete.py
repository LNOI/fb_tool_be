from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import message_usecase

router = APIRouter()


@router.delete("/{message_id}", response_model=ResponseModel)
async def delete_message(user_id: UUID, message_id: UUID):
    is_deleted = await message_usecase.delete_message(message_id)
    if not is_deleted:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND, data=False)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=True)
