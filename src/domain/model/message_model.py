from uuid import UUID

from sqlmodel import ARRAY, Column, Field, String

from src.domain.model.base_model import BaseModel


class TemplateMessageModel(BaseModel, table=True):
    user_id: UUID
    name: str
    content: str
    images: str | None = None
    tags: str | None = None


class MessageModel(BaseModel, table=True):
    user_id: UUID
    template_id: UUID = Field(
        foreign_key="template_message.id", default=None, nullable=True
    )
    content: str
    link_images: list[str] = Field(sa_column=Column(ARRAY(String)), default=[])
    receiver_user_name: str
    receiver_user_profile: str
    tags: list[str] = Field(sa_column=Column(ARRAY(String)), default=[])

