from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.verification_token_model import VerificationTokenModel
from src.domain.repository.db_repository import DBRepository


class VerificationTokenService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_vt(self, vt: VerificationTokenModel) -> VerificationTokenModel:
        return await self.db_repository.insert_item(vt)

    async def get_vt(self, user_id: UUID) -> VerificationTokenModel:
        return await self.db_repository.get_item(VerificationTokenModel, user_id)

    async def update_vt(self, vt: VerificationTokenModel) -> VerificationTokenModel:
        return await self.db_repository.update_item(vt)

    async def delete_vt(self, user_id: UUID) -> bool:
        return await self.db_repository.delete_item(VerificationTokenModel, user_id)

    async def query_vt(self, filter_query: Select) -> List[VerificationTokenModel]:
        return await self.db_repository.query_item(filter_query)

    async def query_verificationToken(
        self, filter_query: Select
    ) -> List[VerificationTokenModel]:
        return await self.db_repository.query_items(filter_query)
