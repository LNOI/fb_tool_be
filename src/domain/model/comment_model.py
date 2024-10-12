from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime

from src.domain.model.base_model import BaseModel


class CommentFacebookModel(BaseModel, table=True):
    post_id: UUID = Field(foreign_key="post_facebook.id")
    user_id: UUID
    content: str | None = None
    images: str | None = None
    sender_name: str | None = None
    sender_link: str | None = None
    note: str | None = None
    comment_date: str | None = None
    last_sync: datetime | None = None
