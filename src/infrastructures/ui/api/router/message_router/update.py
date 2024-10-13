from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.application.dto.message_dto.message_request_dto import UpdateMessageRequestDto
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import message_usecase

router = APIRouter()


@router.put("/{message_id}", response_model=ResponseModel)
async def update_message(
    user_id: UUID, message_id: UUID, message_update: UpdateMessageRequestDto
):
    message = await message_usecase.get_message(message_id)

    if message is None:
        return CustomJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, message="Message not found"
        )

    for key, value in message_update.model_dump().items():
        if value:
            message.__setattr__(key, value)

    result = await message_usecase.update_message(message)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
