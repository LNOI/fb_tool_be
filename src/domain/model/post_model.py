import enum
from datetime import datetime
from uuid import UUID

from sqlmodel import ARRAY, Column, Enum, Field, String
from sqlmodel import Relationship,Field
from src.domain.model.base_model import BaseModel
from src.domain.model.history_scrape_model import HistoryScrapeModel 


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
    hc_id : UUID = Field(foreign_key="history_scrape.id",default=None,nullable=True)
    history_scrape : HistoryScrapeModel = Relationship(back_populates="list_post")