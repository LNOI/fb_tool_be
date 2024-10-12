from math import ceil
from typing import Any, Callable, Dict, List, TypeVar

from src.domain.model.paginate_data_model import PaginatedDataModel
from src.domain.model.base_model import  BaseModel
T = TypeVar("T", bound=BaseModel)


def paginate(
    items: List[T], page: int, page_size: int
) -> PaginatedDataModel[T]:
    start = (page - 1) * page_size
    end = start + page_size

    total_items = len(items)
    total_pages = ceil(total_items / page_size)

    return PaginatedDataModel(
        items=items[start:end],
        total=total_items,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )
