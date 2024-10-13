from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.application.dto.message_dto.message_request_dto import CreateMessageRequestDto
from src.domain.model.message_model import MessageModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import message_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_message(user_id: UUID, message: CreateMessageRequestDto):
    item: MessageModel = MessageModel(**message.model_dump(), user_id=user_id)
    result = await message_usecase.create_message(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
