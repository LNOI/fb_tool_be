from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.application.dto.post_dto.post_request_dto import CreatePostRequestDto
from src.domain.model.post_model import PostModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import post_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_post(user_id: UUID, post: CreatePostRequestDto):
    item: PostModel = PostModel(**post.model_dump())
    result = await post_usecase.create_post(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
