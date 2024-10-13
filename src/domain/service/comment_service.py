from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.comment_model import CommentModel
from src.domain.repository.db_repository import DBRepository


class CommentService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_comment(self, comment: CommentModel) -> CommentModel:
        return await self.db_repository.insert_item(comment)

    async def get_comment(self, comment_id: UUID) -> CommentModel:
        return await self.db_repository.get_item(CommentModel, comment_id)

    async def update_comment(self, comment: CommentModel) -> CommentModel:
        return await self.db_repository.update_item(comment)

    async def delete_comment(self, comment_id: UUID) -> bool:
        return await self.db_repository.delete_item(CommentModel, comment_id)

    async def query_comments(self, filter_query: Select) -> List[CommentModel]:
        return await self.db_repository.query_item(filter_query)
