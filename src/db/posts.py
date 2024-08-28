from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime


class PostFacebook(SQLModel, table=True):
    __tablename__ = "post_facebook"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    group_id: UUID = Field(default=None, foreign_key="group_facebook.id")
    user_id: UUID = Field(default=None, foreign_key="users.id")
    title: str | None = None
    images: str | None = None
    video: str | None = None
    link: str | None = None
    reaction: str | None = None
    owner_name: str | None = None
    profile_owner_post: str = None
    post_date: str | None = None
    last_sync: datetime | None = None
