from uuid import UUID

from pydantic import BaseModel


class CreateMessageRequestDto(BaseModel):
    template_id: UUID | None = None
    content: str
    link_images: list[str] = []
    receiver_user_name: str
    receiver_user_profile: str
    tags: list[str] = []


class UpdateMessageRequestDto(CreateMessageRequestDto):
    pass
