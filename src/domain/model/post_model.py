import enum
from datetime import datetime
from uuid import UUID

from sqlmodel import ARRAY, Column, Enum, Field, String

from src.domain.model.base_model import BaseModel


class PostType(str, enum.Enum):
    CRAWL = "CRAWL"
    AUTO_POST = "AUTO_POST"


class PostModel(BaseModel, table=True):
    group_id: UUID = Field(default=None, foreign_key="group.id", nullable=True)
    user_id: UUID
    title: str | None = None
    link_images: list[str] | None = Field(sa_column=Column(ARRAY(String)))
    link_post: str | None = None
    reaction: int | None = 0
    owner_name: str | None = None
    owner_link: str | None = None
    post_date: datetime | None = None
    last_sync: datetime | None = None
    comments: list[str]  = Field(sa_column=Column(ARRAY(String)),default=[])
    type: PostType = Field(sa_column=Column(Enum(PostType)))
