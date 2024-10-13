from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.post_model import PostModel
from src.domain.service.post_service import PostService


class PostUseCase:
    @inject
    def __init__(self, post_service: PostService):
        self._post_service: PostService = post_service

    async def create_post(self, post: PostModel) -> PostModel:
        return await self._post_service.create_post(post)

    async def get_post(self, post_id: UUID) -> PostModel:
        return await self._post_service.get_post(post_id)

    async def update_post(self, post: PostModel) -> PostModel:
        return await self._post_service.update_post(post)

    async def delete_post(self, post_id: UUID) -> PostModel:
        return await self._post_service.delete_post(post_id)

    async def query_post(self, filter_query: Select):
        return await self._post_service.query_posts(filter_query)
