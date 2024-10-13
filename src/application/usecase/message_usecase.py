from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.message_model import MessageModel
from src.domain.service.message_service import MessageService


class MessageUseCase:
    @inject
    def __init__(self, message_service: MessageService):
        self._message_service: MessageService = message_service

    async def create_message(self, message: MessageModel) -> MessageModel:
        return await self._message_service.create_message(message)

    async def get_message(self, message_id: UUID) -> MessageModel:
        return await self._message_service.get_message(message_id)

    async def update_message(self, message: MessageModel) -> MessageModel:
        return await self._message_service.update_message(message)

    async def delete_message(self, message_id: UUID) -> MessageModel:
        return await self._message_service.delete_message(message_id)

    async def query_message(self, filter_query: Select):
        return await self._message_service.query_messages(filter_query)
