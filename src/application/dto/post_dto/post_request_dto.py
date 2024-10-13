from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from src.domain.model.post_model import PostType

class CreatePostRequestDto(BaseModel):
    group_id: UUID | None = None
    user_id: UUID
    title: str = ""
    link_images: list[str] = []
    link_post: str
    number_of_reaction: int = 0
    owner_name: str
    owner_link: str
    post_date: datetime = datetime.now()
    last_sync: datetime = datetime.now()
    type: PostType

class UpdatePostRequestDto(CreatePostRequestDto):
    pass