from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.accounts_model import AccountsModel
from src.domain.repository.db_repository import DBRepository


class AccountsService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_account(self, account: AccountsModel) -> AccountsModel:
        return await self.db_repository.insert_item(account)

    async def get_account(self, user_id: UUID) -> AccountsModel:
        return await self.db_repository.get_item(AccountsModel, user_id)

    async def update_account(self, account: AccountsModel) -> AccountsModel:
        return await self.db_repository.update_item(account)

    async def delete_account(self, user_id: UUID) -> bool:
        return await self.db_repository.delete_item(AccountsModel, user_id)

    async def query_account(self, filter_query: Select) -> List[AccountsModel]:
        return await self.db_repository.query_item(filter_query)

    async def query_accounts(self, filter_query: Select) -> List[AccountsModel]:
        return await self.db_repository.query_items(filter_query)

    async def get_account_by_session_token(self, session_token: str) -> AccountsModel:
        return await self.db_repository.get_item_by_column(
            AccountsModel, "session_token", session_token
        )
