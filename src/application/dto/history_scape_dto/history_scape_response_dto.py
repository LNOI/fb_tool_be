from uuid import UUID
from src.domain.model.history_scrape_model import StatusScrape
from pydantic import BaseModel
from datetime import datetime
from src.domain.model.group_model import GroupModel
from src.domain.model.post_model import PostModel
    
class HistoryScrapeResponseDto(BaseModel):
    id: UUID
    user_id: UUID
    keyword : str | None = None 
    list_group: list[GroupModel] | None = None
    list_post: list[PostModel] | None = None
    status: StatusScrape
    created_at: datetime
    updated_at: datetime