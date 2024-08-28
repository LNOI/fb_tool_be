from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime


class CommentFacebook(SQLModel, table=True):
    __tablename__ = "comment_facebook"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    post_id: UUID = Field(foreign_key="post_facebook.id")
    user_id: UUID = Field(foreign_key="users.id")
    content: str | None = None
    images: str | None = None
    owner_name: str
    owner_link: str | None = None
    note: str | None = None
    last_sync: datetime | None = None
