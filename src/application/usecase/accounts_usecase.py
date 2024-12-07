from uuid import UUID
from typing import List
from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.accounts_model import AccountsModel
from src.domain.service.accounts_service import AccountsService


class AccountsUseCase:
    @inject
    def __init__(self, account_service: AccountsService):
        self._accounts_service: AccountsService = account_service

    async def create_account(self, account: AccountsModel) -> AccountsModel:
        return await self._accounts_service.create_account(account)

    async def get_account(self, account_id: UUID) -> AccountsModel:
        return await self._accounts_service.get_account(account_id)

    async def update_account(self, account: AccountsModel) -> AccountsModel:
        return await self._accounts_service.update_account(account)

    async def delete_account(self, account_id: UUID) -> AccountsModel:
        return await self._accounts_service.delete_account(account_id)

    async def query_account(self, filter_query: Select) -> AccountsModel:
        return await self._accounts_service.query_account(filter_query)

    async def query_accounts(self, filter_query: Select) -> List[AccountsModel]:
        return await self._accounts_service.query_accounts(filter_query)
