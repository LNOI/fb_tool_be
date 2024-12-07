from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class SessionsModel(SQLModel, table=True):
    __tablename__ = "sessions"
    id: int | None = Field(primary_key=True, default=None)
    userId: UUID
    expires: datetime
    sessionToken: str
