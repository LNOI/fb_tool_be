from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import post_usecase

router = APIRouter()


@router.delete("/{post_id}", response_model=ResponseModel)
async def delete_post(post_id: UUID):
    is_deleted = await post_usecase.delete_post(post_id)
    if not is_deleted:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND, data=False)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=True)
