from uuid import UUID
from sqlmodel import  Field, Column,Enum,String,ARRAY
from datetime import datetime
import enum

from src.domain.model.base_model import BaseModel


class PostType(str, enum.Enum):
    CRAWL = "crawl"
    AUTO_POST = "auto_post"


class PostModel(BaseModel, table=True):
    group_id: UUID = Field(default=None, foreign_key="group.id", nullable=True)
    user_id: UUID
    title: str | None = None
    link_images: list[str] | None = Field(sa_column=Column(ARRAY(String)))
    link_post: str | None = None
    number_of_reaction: int | None = 0
    owner_name: str | None = None
    owner_link: str | None = None
    post_date: datetime | None = None
    last_sync: datetime | None = None
    type: PostType = Field(sa_column=Column(Enum(PostType)))
