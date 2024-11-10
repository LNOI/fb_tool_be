from datetime import datetime
from uuid import UUID

from sqlmodel import Relationship,Field

from src.domain.model.base_model import BaseModel
from src.domain.model.post_model import PostModel
from src.domain.model.history_scrape_model import HistoryScrapeModel
from enum import Enum

class StatusGroupScrape(str,Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    

class GroupModel(BaseModel, table=True):
    user_id: UUID
    link_group: str = Field(unique=True,nullable=False)
    name: str
    description: str | None = None
    privacy: str  #  Công khai | Riêng tư
    members: str  #  69K thành viên  | split  69k
    post_per_day: str
    user_admin: str | None = None
    is_member: bool | None = False
    tags: str | None = None
    last_sync: datetime | None = None
    session_id : str | None = None
    status : StatusGroupScrape = Field(default=StatusGroupScrape.PENDING)
    hc_id : UUID = Field(foreign_key="history_scrape.id",default=None,nullable=True)
    history_scrape: HistoryScrapeModel = Relationship(back_populates="list_group")
    posts: list[PostModel] = Relationship()
    