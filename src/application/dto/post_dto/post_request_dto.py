from datetime import datetime
from uuid import UUID
from typing import Union
from pydantic import BaseModel

from src.domain.model.post_model import PostType


class CreatePostRequestDto(BaseModel):
    group_id: UUID | None = None
    title: str = ""
    link_images: list[str] = []
    link_post: str
    owner_link: str
    reaction: Union[int, str] = 0
    owner_name: str
    post_date: int = 0
    type: PostType
    comments: list[str] = []

class UpdatePostRequestDto(CreatePostRequestDto):
    pass
