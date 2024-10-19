from datetime import datetime
from uuid import UUID

from sqlmodel import Relationship,Field

from src.domain.model.base_model import BaseModel
from src.domain.model.post_model import PostModel


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
    posts: list[PostModel] = Relationship()
