from typing import List
from black import datetime
from pydantic import BaseModel, Field

class CreateCommentRequestDto(BaseModel):
    content: str | None = None
    images: List[str] | None = None
    sender_name: str
    sender_link: str
    comment_date: datetime | None = None

class UpdateCommentRequestDto(CreateCommentRequestDto):
    pass
