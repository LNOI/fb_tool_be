from uuid import UUID
from typing import List, TypeVar, Generic, Dict, Any
from sqlmodel.sql._expression_select_cls import Select
from abc import ABC, abstractmethod


from src.domain.model.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)
class DBRepository(ABC, Generic[T]):
    @abstractmethod
    async def insert_item(self, item: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def insert_items(self, items: List[T]) -> List[T]:
        raise NotImplementedError()

    @abstractmethod
    async def get_item(self,model:T, uuid: UUID ) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def update_item(self, item: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def delete_item(self, model:T,  uuid: UUID) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def query_item(self,filter_query: Select) -> List[T]:
        raise NotImplementedError()
