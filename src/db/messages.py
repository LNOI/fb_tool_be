from uuid import UUID
from sqlmodel import SQLModel, Field
from datetime import datetime


class MessagesFacebook(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    user_id: UUID = Field(default=None, foreign_key="users.id")
    content: str
    images: str
    receiver_user_name: str
    receiver_user_profile: str
    created_at: datetime = Field(default=datetime.now())
