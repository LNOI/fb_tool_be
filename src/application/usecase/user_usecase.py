from typing import Any, Dict, List, Optional ,TypeVar
from uuid import UUID
from injector import inject
from sqlmodel.sql._expression_select_cls import Select
from src.domain.model.user_model import UserModel
from src.domain.service.user_service import UserService

class UserUseCase:
    @inject
    def  __init__(self, user_service: UserService):
        self._user_service: UserService = user_service

    async def create_user(self, user: UserModel)->UserModel:
        return await self._user_service.create_user(user)

    async def get_user(self, user_id: UUID)->UserModel:
        return await self._user_service.get_user(user_id)

    async def update_user(self, user: UserModel)->UserModel:
        return await self._user_service.update_user(user)

    async def delete_user(self, user_id: UUID)->UserModel:
        return await self._user_service.delete_user(user_id)

    async def query_user(self, filter_query: Select):
        return await self._user_service.query_users(filter_query)



