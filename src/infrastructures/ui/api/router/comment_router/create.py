from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.application.dto.comment_dto.comment_request_dto import CreateCommentRequestDto
from src.domain.model.comment_model import CommentModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import comment_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_comment(user_id: UUID, comment: CreateCommentRequestDto):
    item: CommentModel = CommentModel(**comment.model_dump())
    result = await comment_usecase.create_comment(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
