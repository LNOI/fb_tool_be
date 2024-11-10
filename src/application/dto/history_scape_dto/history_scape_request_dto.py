from uuid import UUID
from src.domain.model.history_scrape_model import StatusScrape
from pydantic import BaseModel

    
class CreateHistoryScrapeRequestDto(BaseModel):
    keyword : str

class UpdateHistoryScrapeRequestDto(BaseModel):
    status : StatusScrape
    list_group: list[UUID] | None = None
    list_post: list[UUID] | None = None