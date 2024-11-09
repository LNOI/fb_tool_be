from uuid import UUID

from sqlmodel import Field,Column,ARRAY

from src.domain.model.base_model import BaseModel

class ProcessAutoModel(BaseModel, table=True):
    user_id: UUID
    list_group: list[UUID] = Field(sa_column=Column(ARRAY(UUID)),default=[])
    list_post: list[UUID] = Field(sa_column=Column(ARRAY(UUID)),default=[])
    list_comment: list[UUID] = Field(sa_column=Column(ARRAY(UUID)),default=[])
