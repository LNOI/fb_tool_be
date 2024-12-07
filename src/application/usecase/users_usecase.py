from uuid import UUID
from typing import List
from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.users_model import UsersModel
from src.domain.service.users_service import UsersService


class UsersUseCase:
    @inject
    def __init__(self, user_service: UsersService):
        self._users_service: UsersService = user_service

    async def create_user(self, user: UsersModel) -> UsersModel:
        return await self._users_service.create_user(user)

    async def get_user(self, user_id: UUID) -> UsersModel:
        return await self._users_service.get_user(user_id)

    async def update_user(self, user: UsersModel) -> UsersModel:
        return await self._users_service.update_user(user)

    async def delete_user(self, user_id: UUID) -> UsersModel:
        return await self._users_service.delete_user(user_id)

    async def query_user(self, filter_query: Select) -> UsersModel:
        return await self._users_service.query_user(filter_query)

    async def query_users(self, filter_query: Select) -> List[UsersModel]:
        return await self._users_service.query_users(filter_query)
