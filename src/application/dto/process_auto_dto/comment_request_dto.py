from typing import List

from pydantic import BaseModel, Field


class CreateProcessAutoRequestDto(BaseModel):
    list_post : List[str] = Field(default=[])
    list_group : List[str] = Field(default=[])
    list_comment : List[str] = Field(default=[])


class UpdateProcessAutoRequestDto(CreateProcessAutoRequestDto):
    pass

