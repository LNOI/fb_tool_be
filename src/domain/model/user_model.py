from typing import Optional

from sqlmodel import Field, Column, String, ARRAY

from src.domain.model.base_model import BaseModel


class UserModel(BaseModel, table=True):
    name: str = Field(description="Username")
    email: str = Field(description="Email")
    avatar: Optional[str] = Field(description="Avatar")
    scopes: list[str] = Field(sa_column=Column(ARRAY(String)), default=["me"])
    is_active: bool = True
