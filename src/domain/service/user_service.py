from typing import  Dict, Any, Type, List
from injector import inject
from uuid import UUID
from src.domain.repository.db_repository import DBRepository
from src.domain.model.user_model import  UserModel
from sqlmodel.sql._expression_select_cls import Select
class UserService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_user(self, user: UserModel)->UserModel:
        return await self.db_repository.insert_item(user)

    async def get_user(self, user_id: UUID)->UserModel:
        return await self.db_repository.get_item(UserModel,user_id)

    async def update_user(self, user: UserModel)->UserModel:
        return await self.db_repository.update_item(user)

    async  def delete_user(self, user_id: UUID)->bool:
        return await self.db_repository.delete_item(UserModel,user_id )

    async def query_users(self, filter_query: Select )->List[UserModel]:
        return await self.db_repository.query_item(filter_query)