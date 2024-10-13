import re
from datetime import datetime
from functools import partial
from uuid import UUID, uuid4

from sqlalchemy.orm import declared_attr
from sqlmodel import Field, SQLModel

_snake_1 = partial(re.compile(r"(.)((?<![^A-Za-z])[A-Z][a-z]+)").sub, r"\1_\2")
_snake_2 = partial(re.compile(r"([a-z0-9])([A-Z])").sub, r"\1_\2")


def snake_case(string: str) -> str:
    return _snake_2(_snake_1(string))


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=True)
    deleted_at: datetime | None = Field(default=None)

    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__).lower().replace("_model", "")

    __table_args__ = {
        "extend_existing": True
    }  # use to fix change name of table sqlmodel
