from uuid import UUID
import re
from fastapi import APIRouter
from starlette import status
from datetime import datetime
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
    # get number reaction from post.reactions from string with regex
    try:
        if post.reaction and isinstance(post.reaction, str):
            post.reaction = int(re.findall(r'\d+', post.reaction)[0])
    except Exception as e:
        print(e)
        post.reaction = 0

    if not post.post_date:
        post.post_date = datetime.now()
    item: PostModel = PostModel(**post.model_dump(),user_id=user_id,last_sync=datetime.now())
    result = await post_usecase.create_post(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
