from typing import Optional

from pydantic import BaseModel

class CreateUserRequestDto(BaseModel):
    username : str
    email : str
    avatar: Optional[str]
    is_active : bool = True

class UpdateUserRequestDto(BaseModel):
    username: str
    email: str
    avatar: Optional[str]
    is_active: bool = True
