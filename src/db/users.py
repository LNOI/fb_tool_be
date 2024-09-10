from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str
    email: str
    avatar: str | None = None
    is_active: bool = True
