from uuid import UUID
from fastapi import APIRouter
from starlette import status

from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import post_usecase

router = APIRouter()

@router.get('/{post_id}', response_model=ResponseModel)
async def get_post(post_id: UUID):
    post = await post_usecase.get_post(post_id)
    if not post:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    return CustomJSONResponse(
        status_code=status.HTTP_200_OK,
        data=post
    )
