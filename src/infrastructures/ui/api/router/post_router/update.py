from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.application.dto.post_dto.post_request_dto import UpdatePostRequestDto
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import post_usecase

router = APIRouter()


@router.put("/{post_id}", response_model=ResponseModel)
async def update_post(user_id: UUID, post_id: UUID, post_update: UpdatePostRequestDto):
    post = await post_usecase.get_post(post_id)

    if post is None:
        return CustomJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, message="post not found"
        )

    for key, value in post_update.model_dump().items():
        if value:
            post.__setattr__(key, value)

    result = await post_usecase.update_post(post)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
