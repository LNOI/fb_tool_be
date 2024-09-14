from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from src.db.posts import PostFacebook


class GroupFacebook(SQLModel, table=True):
    __tablename__ = "group_facebook"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID
    link_group: str | None = None
    name: str
    description: str | None = None
    privacy: str  #  Công khai | Riêng tư
    members: str  #  69K thành viên  | split  69k
    post_per_day: str
    user_admin: str | None = None
    is_member: bool | None = False
    tags: str | None = None
    last_sync: datetime | None = None
    deleted: bool | None = False
    posts: list[PostFacebook] = Relationship()
