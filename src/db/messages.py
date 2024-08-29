from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime


class TemplateMessage(SQLModel, table=True):
    __tablename__ = "template_message"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id", default=None, nullable=True)
    name: str
    content: str
    images: str | None = None
    tags: str | None = None
    last_update: datetime = Field(default=datetime.now())


class MessagesFacebook(SQLModel, table=True):
    __tablename__ = "messages_facebook"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id")
    template_id: UUID = Field(
        foreign_key="template_message.id", default=None, nullable=True
    )
    content: str
    images: str
    receiver_user_name: str
    receiver_user_profile: str
    tags: str | None = None
    created_at: datetime = Field(default=datetime.now())
