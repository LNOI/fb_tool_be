from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from src.application.dto.comment_dto.comment_request_dto import CreateCommentRequestDto, CreateCommentRequestAdminDto
from src.domain.model.comment_model import CommentModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.utils.auth import validate_session_token
from src.middleware import comment_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_comment( comment: CreateCommentRequestDto, user_id: UUID = Depends(validate_session_token)):
    item = CommentModel(**comment.model_dump(), user_id=user_id)
    result = await comment_usecase.create_comment(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)


# Endpoint for admin
@router.post("/admin", response_model=ResponseModel)
async def create_comment_admin(comment: CreateCommentRequestAdminDto):
    item = CommentModel(**comment.model_dump())
    result = await comment_usecase.create_comment(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)