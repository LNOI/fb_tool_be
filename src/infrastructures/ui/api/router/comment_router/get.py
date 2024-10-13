from uuid import UUID
from fastapi import APIRouter
from select import select
from starlette import status

from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import comment_usecase

router = APIRouter()

@router.get('/{comment_id}', response_model=ResponseModel)
async def get_comment(comment_id: UUID):
    comment = await comment_usecase.get_comment(comment_id)
    if not comment:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    return CustomJSONResponse(
        status_code=status.HTTP_200_OK,
        data=comment
    )
