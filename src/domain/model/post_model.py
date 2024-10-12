from uuid import UUID
from sqlmodel import  Field
from datetime import datetime
from enum import Enum

from src.domain.model.base_model import BaseModel


class PostType(str, Enum):
    CRAWL = "crawl"
    AUTO_POST = "auto_post"


class PostFacebookModel(BaseModel, table=True):
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
