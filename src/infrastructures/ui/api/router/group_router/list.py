from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Security
from sqlmodel import select
from starlette import status

from src.domain.model.group_model import GroupModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.paginate import paginate
from src.middleware import group_usecase

router = APIRouter()


@router.get(
    "/",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def list_group(user_id: UUID, page: int = 1, page_size: int = 25):
    query = (
        select(GroupModel)
        .where(GroupModel.user_id == user_id)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .order_by(GroupModel.created_at.desc())
    )
    result = await group_usecase.query_group(filter_query=query)

    result = paginate(
        items=result,
        page=page,
        page_size=page_size,
    )
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
