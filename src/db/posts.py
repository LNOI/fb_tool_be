from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum


class PostType(str, Enum):
    CRAWL = "crawl"
    AUTO_POST = "auto_post"


class PostFacebook(SQLModel, table=True):
    __tablename__ = "post_facebook"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    group_id: UUID = Field(default=None, foreign_key="group_facebook.id", nullable=True)
    user_id: UUID
    title: str | None = None
    link_images: str | None = None
    link_post: str | None = None
    number_of_reaction: int | None = 0
    owner_name: str | None = None
    owner_link: str | None = None
    post_date: str | None = None
    last_sync: datetime | None = None
    type: str | None = PostType.CRAWL.value
    deleted: bool | None = False
