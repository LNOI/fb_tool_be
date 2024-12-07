from uuid import UUID

from fastapi import APIRouter
from sqlmodel import select
from starlette import status

from src.domain.model.post_model import PostModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.paginate import paginate
from src.middleware import post_usecase

router = APIRouter()


@router.get("/", response_model=ResponseModel)
async def list_post(user_id: UUID, hc_id: UUID, page: int = 1, page_size: int = 25):
    query = (
        select(PostModel)
        .where(PostModel.user_id == user_id)
        .where(PostModel.deleted_at.is_(None))
    )
    if hc_id:
        query = query.where(PostModel.hc_id == hc_id)

    query = (
        query.offset((page - 1) * page_size)
        .limit(page_size)
        .order_by(PostModel.created_at.desc())
    )

    result = await post_usecase.query_post(filter_query=query)

    result = paginate(
        items=result,
        page=page,
        page_size=page_size,
    )
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
