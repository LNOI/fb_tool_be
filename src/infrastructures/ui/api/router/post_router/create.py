from uuid import UUID
from fastapi import APIRouter
from starlette import status
from datetime import datetime
from src.application.dto.post_dto.post_request_dto import CreatePostRequestDto, CreatePostRequestAdminDto
from src.domain.model.post_model import PostModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import post_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_post(user_id: UUID, post: CreatePostRequestDto):
    # get number reaction from post.reactions from string with regex
    if not post.post_date:
        post.post_date = datetime.now()
    item: PostModel = PostModel(**post.model_dump(), user_id=user_id)
    result = await post_usecase.create_post(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)


@router.post("/admin", response_model=ResponseModel)
async def create_post_admin(post: CreatePostRequestAdminDto):
    if not post.post_date:
        post.post_date = datetime.now()
    item = PostModel(**post.model_dump())
    result = await post_usecase.create_post(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)