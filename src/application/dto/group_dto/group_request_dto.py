from uuid import UUID

from pydantic import BaseModel


class CreateGroupRequestDto(BaseModel):
    name: str
    link_group: str | None = None
    description: str | None = None
    privacy: str  # Công khai | Riêng tư
    members: str  # 69K thành viên  | split  69k
    post_per_day: str
    user_admin: str | None = None
    is_member: bool | None = False
    tags: str | None = None
    hc_id: UUID | None = None

class UpdateGroupRequestDto(CreateGroupRequestDto):
    pass
