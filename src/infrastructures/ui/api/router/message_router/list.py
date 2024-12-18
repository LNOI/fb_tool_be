from uuid import UUID

from fastapi import APIRouter
from sqlmodel import select
from starlette import status

from src.domain.model.message_model import MessageModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.paginate import paginate
from src.middleware import message_usecase

router = APIRouter()


@router.get("/", response_model=ResponseModel)
async def list_message(user_id: UUID, page: int = 1, page_size: int = 25):
    query = (
        select(MessageModel)
        .where(MessageModel.user_id == user_id)
        .limit(page_size)
        .offset((page - 1) * page_size)
        .order_by(MessageModel.created_at.desc())
    )
    result = await message_usecase.query_message(filter_query=query)

    result = paginate(
        items=result,
        page=page,
        page_size=page_size,
    )
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
