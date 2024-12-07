from uuid import UUID
from pydantic import BaseModel, Field


class CreatePostRequestDto(BaseModel):
    group_id: UUID | None = None
    title: str | None = None
    link: str
    images: list[str] = Field(default=[])
    owner_name: str
    owner_link: str
    reaction: int | None = None
    comments: list[dict] = Field(default=[])
    post_date: int = 0
    hc_id: UUID

class CreatePostRequestAdminDto(CreatePostRequestDto):
    user_id : UUID

class UpdatePostRequestDto(CreatePostRequestDto):
    pass
