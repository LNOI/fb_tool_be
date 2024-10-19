from math import ceil
from typing import Any, Callable, Dict, List, TypeVar

from src.domain.model.base_model import BaseModel
from src.domain.model.paginate_data_model import PaginatedDataModel

T = TypeVar("T", bound=BaseModel)


def paginate(items: List[T], page: int, page_size: int) -> PaginatedDataModel[T]:
    return PaginatedDataModel(
        items=items,
        total=len(items),
        page=page,
        page_size=page_size,
        total_pages=0,
    )
