from typing import List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.sessions_model import SessionsModel
from src.domain.repository.db_repository import DBRepository


class SessionsService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def get_session(self, session_token: str) -> SessionsModel:
        return await self.db_repository.get_item_by_column(
            SessionsModel, "sessionToken", session_token
        )
