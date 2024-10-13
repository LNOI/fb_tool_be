from pydantic import BaseModel
from uuid import UUID
class CreateGroupRequestDto(BaseModel):
    user_id: UUID
    link_group: str | None = None
    name: str
    description: str | None = None
    privacy: str  # Công khai | Riêng tư
    members: str  # 69K thành viên  | split  69k
    post_per_day: str
    user_admin: str | None = None
    is_member: bool | None = False
    tags: str | None = None

class UpdateGroupRequestDto(CreateGroupRequestDto):
    pass


