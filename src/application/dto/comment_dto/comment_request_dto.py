from typing import List
from uuid import UUID 

from datetime import datetime
from pydantic import BaseModel, Field


class CreateCommentRequestDto(BaseModel):
    post_id: UUID
    content: str | None = None
    images: List[str] | None = None
    owner_name: str
    owner_link: str
    comment_date: datetime | None = None
    hc_id: UUID

class UpdateCommentRequestDto(CreateCommentRequestDto):
    pass
