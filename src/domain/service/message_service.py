from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.message_model import MessageModel
from src.domain.repository.db_repository import DBRepository


class MessageService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_message(self, message: MessageModel) -> MessageModel:
        return await self.db_repository.insert_item(message)

    async def get_message(self, messages_id: UUID) -> MessageModel:
        return await self.db_repository.get_item(MessageModel, messages_id)

    async def update_message(self, message: MessageModel) -> MessageModel:
        return await self.db_repository.update_item(message)

    async def delete_message(self, messages_id: UUID) -> bool:
        return await self.db_repository.delete_item(MessageModel, messages_id)

    async def query_messages(self, filter_query: Select) -> List[MessageModel]:
        return await self.db_repository.query_item(filter_query)
