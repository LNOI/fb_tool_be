from typing import Optional

from sqlmodel import Field, Column, String, ARRAY
from src.domain.model.base_model import BaseModel
from datetime import datetime


class UsersModel(BaseModel, table=True):
    name: str = Field(description="Username", nullable=True)
    email: str = Field(description="Email", nullable=True)
    image: str = Field(description="Image", nullable=True)
    emailVerified: datetime = Field(nullable=True)
