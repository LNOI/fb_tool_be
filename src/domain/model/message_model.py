from uuid import UUID
from sqlmodel import Field
from src.domain.model.base_model import BaseModel


class TemplateMessageModel(BaseModel, table=True):
    user_id: UUID
    name: str
    content: str
    images: str | None = None
    tags: str | None = None

class MessagesFacebookModel(BaseModel, table=True):
    user_id: UUID
    template_id: UUID = Field(
        foreign_key="template_message.id", default=None, nullable=True
    )
    content: str
    images: str
    receiver_user_name: str
    receiver_user_profile: str
    tags: str | None = None
