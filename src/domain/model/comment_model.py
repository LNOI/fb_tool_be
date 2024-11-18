from datetime import datetime
from uuid import UUID

from sqlmodel import ARRAY, Column, Field, String, Relationship

from src.domain.model.base_model import BaseModel


class CommentModel(BaseModel, table=True):
    post_id: UUID = Field(foreign_key="post.id")
    user_id: UUID
    content: str | None = None
    images: list[str] | None = Field(sa_column=Column(ARRAY(String)),default=[])
    owner_name: str
    owner_link: str
    comment_date: datetime = Field(default_factory=datetime.now, nullable=True)
    hc_id: UUID = Field(foreign_key="history_scrape.id", nullable=False)
    hc_scrape: "HistoryScrapeModel" = Relationship(back_populates="comments")

