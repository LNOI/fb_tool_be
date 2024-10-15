from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class CreateUserRequestDto(BaseModel):
    id : UUID
    name: str
    email: str
    avatar: Optional[str]
    is_active: bool = True


class UpdateUserRequestDto(BaseModel):
    name: Optional[str]
    email: Optional[str]
    avatar: Optional[str]
    is_active: bool = True
