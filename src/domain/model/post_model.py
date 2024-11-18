from datetime import datetime
from uuid import UUID

from sqlmodel import ARRAY, Column, String
from sqlmodel import Field, Relationship
from src.domain.model.base_model import BaseModel

class PostModel(BaseModel, table=True):
    group_id: UUID = Field(default=None, foreign_key="group.id", nullable=True)
    user_id: UUID
    title: str | None = None
    link: str
    images: list[str] | None = Field(sa_column=Column(ARRAY(String)))
    reaction: int  = Field(default=0)
    owner_name: str
    owner_link: str
    post_date: datetime | None = None
    hc_id : UUID = Field(foreign_key="history_scrape.id",nullable=False)
    hc_scrape: "HistoryScrapeModel" = Relationship(back_populates="posts")