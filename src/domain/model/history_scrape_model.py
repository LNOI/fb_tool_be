from uuid import UUID

from sqlmodel import  Relationship,Field

from src.domain.model.base_model import BaseModel

class HistoryScrapeModel(BaseModel, table=True):
    user_id: UUID
    keyword: str
    num_groups :int = Field(default=0, nullable=True)
    num_posts : int = Field(default=0, nullable=True)
    num_comments : int = Field(default=0, nullable=True)
    groups : list["GroupModel"] = Relationship(back_populates="hc_scrape")
    posts: list["PostModel"] = Relationship(back_populates="hc_scrape")
    comments :  list["CommentModel"] = Relationship(back_populates="hc_scrape")



