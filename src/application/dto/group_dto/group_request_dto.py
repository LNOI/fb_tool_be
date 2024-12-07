from uuid import UUID
from pydantic import BaseModel


class CreateGroupRequestDto(BaseModel):
    name: str
    link: str
    description: str | None = None
    privacy: str  # Công khai | Riêng tư
    members: str  # 69K thành viên  | split  69k
    posting_frequency: str
    is_member: bool = False
    user_admin: str | None = None
    hc_id: UUID

class CreateGroupRequestAdminDto(CreateGroupRequestDto):
    user_id : UUID


class UpdateGroupRequestDto(CreateGroupRequestDto):
    pass
