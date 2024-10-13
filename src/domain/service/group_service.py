from typing import  Dict, Any, Type, List
from injector import inject
from uuid import UUID
from src.domain.repository.db_repository import DBRepository
from src.domain.model.group_model import GroupModel
from sqlmodel.sql._expression_select_cls import Select

class GroupFacebookService:
    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_group(self, group: GroupModel)->GroupModel:
        return await self.db_repository.insert_item(group)

    async def get_group(self, group_id: UUID)->GroupModel:
        return await self.db_repository.get_item(GroupModel,group_id)

    async def update_group(self, group: GroupModel)->GroupModel:
        return await self.db_repository.update_item(group)

    async  def delete_group(self, group_id: UUID)->bool:
        return await self.db_repository.delete_item(GroupModel,group_id )

    async def query_groups(self, filter_query: Select )->List[GroupModel]:
        return await self.db_repository.query_item(filter_query)