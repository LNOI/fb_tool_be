from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class HistoryScrapeResponseDto(BaseModel):
    id: UUID
    user_id: UUID
    keyword : str
    created_at: datetime
    updated_at: datetime
    groups : list[dict] = None
    posts : list[dict] = None
    comments : list[dict] = None
