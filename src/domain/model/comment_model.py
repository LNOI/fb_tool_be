from datetime import datetime
from uuid import UUID

from sqlmodel import ARRAY, Column, Field, String

from src.domain.model.base_model import BaseModel


class CommentModel(BaseModel, table=True):
    post_id: UUID = Field(foreign_key="post.id")
    user_id: UUID
    content: str | None = None
    images: list[str] | None = Field(sa_column=Column(ARRAY(String)))
    sender_name: str | None = None
    sender_link: str | None = None
    note: str | None = None
    comment_date: datetime = Field(default_factory=datetime.now, nullable=True)


