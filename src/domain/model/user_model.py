from typing import Optional

from sqlmodel import Field

from src.domain.model.base_model import BaseModel


class UserModel(BaseModel, table=True):
    username: str = Field(description="Username")
    email: str = Field(description="Email")
    avatar: Optional[str] = Field(description="Avatar")
    is_active: bool = True
