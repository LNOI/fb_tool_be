from uuid import UUID
from sqlmodel import Field, ARRAY, Column, String
from src.domain.model.base_model import BaseModel
from enum import Enum

class StatusScrape(str, Enum):
    GROUP = "group"
    POST = "post"
    START = "start"
    FAILED = "failed"
    SUCCESS = "success"

class HistoryScrapeModel(BaseModel, table=True):
    user_id: UUID
    list_group: list[UUID] = Field(sa_column=Column(ARRAY(String)),default=[])
    list_post: list[UUID] = Field(sa_column=Column(ARRAY(String)),default=[])
    status: StatusScrape = Field(default=StatusScrape.START)
    