from uuid import UUID

from sqlmodel import Field, Relationship

from src.domain.model.base_model import BaseModel


class GroupModel(BaseModel, table=True):
    user_id: UUID
    link: str
    name: str
    description: str | None = None
    privacy: str  #  Công khai | Riêng tư
    members: str  #  69K thành viên  | split  69k
    posting_frequency: str
    is_member: bool = False
    user_admin: str | None = None
    hc_id: UUID = Field(foreign_key="history_scrape.id", nullable=False)
    hc_scrape: "HistoryScrapeModel" = Relationship(back_populates="groups")