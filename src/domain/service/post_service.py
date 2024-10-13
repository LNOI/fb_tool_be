from typing import List
from injector import inject
from uuid import UUID
from src.domain.repository.db_repository import DBRepository
from src.domain.model.post_model import PostModel
from sqlmodel.sql._expression_select_cls import Select
class PostService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_post(self, post: PostModel)->PostModel:
        return await self.db_repository.insert_item(post)

    async def get_post(self, post_id: UUID)->PostModel:
        return await self.db_repository.get_item(PostModel,post_id)

    async def update_post(self, post: PostModel)->PostModel:
        return await self.db_repository.update_item(post)

    async  def delete_post(self, post_id: UUID)->bool:
        return await self.db_repository.delete_item(PostModel,post_id )

    async def query_posts(self, filter_query: Select )->List[PostModel]:
        return await self.db_repository.query_item(filter_query)