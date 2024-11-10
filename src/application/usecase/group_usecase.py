from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.group_model import GroupModel
from src.domain.service.group_service import GroupFacebookService


class GroupFacebookUseCase:
    @inject
    def __init__(self, group_service: GroupFacebookService):
        self._group_service: GroupFacebookService = group_service

    async def create_group(self, group: GroupModel) -> GroupModel:
        return await self._group_service.create_group(group)

    async def get_group(self, group_id: UUID) -> GroupModel:
        return await self._group_service.get_group(group_id)

    async def update_group(self, group: GroupModel) -> GroupModel:
        return await self._group_service.update_group(group)

    async def delete_group(self, group_id: UUID) -> GroupModel:
        return await self._group_service.delete_group(group_id)

    async def query_group(self, filter_query: Select):
        return await self._group_service.query_groups(filter_query)
    
    async def query_groups(self, filter_query: Select):
        return await self._group_service.query_groups(filter_query)
