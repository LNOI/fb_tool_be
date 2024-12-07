from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.users_model import UsersModel
from src.domain.repository.db_repository import DBRepository


class UsersService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_user(self, user: UsersModel) -> UsersModel:
        return await self.db_repository.insert_item(user)

    async def get_user(self, user_id: UUID) -> UsersModel:
        return await self.db_repository.get_item(UsersModel, user_id)

    async def update_user(self, user: UsersModel) -> UsersModel:
        return await self.db_repository.update_item(user)

    async def delete_user(self, user_id: UUID) -> bool:
        return await self.db_repository.delete_item(UsersModel, user_id)

    async def query_user(self, filter_query: Select) -> List[UsersModel]:
        return await self.db_repository.query_item(filter_query)

    async def query_users(self, filter_query: Select) -> List[UsersModel]:
        return await self.db_repository.query_items(filter_query)
