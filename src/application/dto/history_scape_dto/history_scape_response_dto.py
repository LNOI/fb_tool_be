from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class HistoryScrapeResponseDto(BaseModel):
    id: UUID
    user_id: UUID
    keyword: str
    created_at: datetime
    updated_at: datetime
    groups: list[dict] = Field(default=[])
    posts: list[dict] = Field(default=[])
    comments: list[dict] = Field(default=[])
