from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.post_model import PostModel
from src.domain.repository.db_repository import DBRepository


class PostService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_post(self, post: PostModel) -> PostModel:
        return await self.db_repository.insert_item(post)

    async def get_post(self, post_id: UUID) -> PostModel:
        return await self.db_repository.get_item(PostModel, post_id)

    async def update_post(self, post: PostModel) -> PostModel:
        return await self.db_repository.update_item(post)

    async def update_posts(self, posts: List[PostModel]) -> List[PostModel]:
        return await self.db_repository.update_items(posts)

    async def delete_post(self, post_id: UUID) -> bool:
        return await self.db_repository.delete_item(PostModel, post_id)

    async def query_posts(self, filter_query: Select) -> List[PostModel]:
        return await self.db_repository.query_items(filter_query)
