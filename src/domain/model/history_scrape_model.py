from uuid import UUID
from sqlmodel import Field, ARRAY, Column, String,Relationship
from src.domain.model.base_model import BaseModel
from typing import List
from enum import Enum

class StatusScrape(str, Enum):
    GROUP = "group"
    POST = "post"
    START = "start"
    FAILED = "failed"
    SUCCESS = "success"

class HistoryScrapeModel(BaseModel, table=True):
    user_id: UUID
    keyword: str | None = None  
    list_group: List["GroupModel"] = Relationship(back_populates="history_scrape")
    list_post: List["PostModel"] = Relationship(back_populates="history_scrape")
    status: StatusScrape = Field(default=StatusScrape.START)
    