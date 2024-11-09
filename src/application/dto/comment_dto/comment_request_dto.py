from typing import List
from uuid import UUID 

from datetime import datetime
from pydantic import BaseModel, Field


class CreateCommentRequestDto(BaseModel):
    post_id: UUID
    content_comment: str | None = None
    images: List[str] | None = None
    sender_name: str
    sender_link: str
    comment_date: datetime | None = None


class UpdateCommentRequestDto(CreateCommentRequestDto):
    pass
