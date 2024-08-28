from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime


class GroupFacebook(SQLModel, table=True):
    __tablename__ = "group_facebook"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id")
    link: str
    name: str
    description: str | None = None
    privacy: str
    members: str
    post_per_day: str
    user_admin: str | None = None
    tags: str | None = None
    last_sync: datetime | None = None
