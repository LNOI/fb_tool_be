from uuid import UUID
from typing import List
from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.comment_model import CommentModel
from src.domain.service.comment_service import CommentService


class CommentUseCase:
    @inject
    def __init__(self, comment_service: CommentService):
        self._comment_service: CommentService = comment_service

    async def create_comment(self, comment: CommentModel) -> CommentModel:
        return await self._comment_service.create_comment(comment)

    async def get_comment(self, comment_id: UUID) -> CommentModel:
        return await self._comment_service.get_comment(comment_id)

    async def update_comment(self, comment: CommentModel) -> CommentModel:
        return await self._comment_service.update_comment(comment)

    async def update_comments(self, comments: List[CommentModel]) -> List[CommentModel]:
        return await self._comment_service.update_comments(comments)

    async def delete_comment(self, comment_id: UUID) -> CommentModel:
        return await self._comment_service.delete_comment(comment_id)

    async def query_comment(self, filter_query: Select):
        return await self._comment_service.query_comments(filter_query)

    async def query_comments(self, filter_query: Select):
        return await self._comment_service.query_comments(filter_query)
