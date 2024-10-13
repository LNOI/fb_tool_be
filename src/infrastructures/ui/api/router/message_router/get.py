from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import message_usecase

router = APIRouter()


@router.get("/{message_id}", response_model=ResponseModel)
async def get_message(user_id: UUID, message_id: UUID):
    message = await message_usecase.get_message(message_id)
    if not message:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=message)
