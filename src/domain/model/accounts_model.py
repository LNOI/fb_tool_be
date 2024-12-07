from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID

from src.domain.model.base_model import BaseModel


class AccountsModel(BaseModel, table=True):
    userId: UUID
    type: str
    provider: str
    providerAccountId: str
    refresh_token: str = Field(nullable=True)
    access_token: str = Field(nullable=True)
    expires_at: int = Field(nullable=True)
    id_token: str = Field(nullable=True)
    scope: str = Field(nullable=True)
    session_state: str = Field(nullable=True)
    token_type: str = Field(nullable=True)
