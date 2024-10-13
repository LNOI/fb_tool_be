from uuid import  UUID
from fastapi import APIRouter
from starlette import status

from src.application.dto.comment_dto.comment_request_dto import UpdateCommentRequestDto
from src.domain.model.comment_model import CommentModel
from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import comment_usecase

router = APIRouter()

@router.put('/{comment_id}', response_model=ResponseModel)
async def update_comment(comment_id : UUID,  comment_update: UpdateCommentRequestDto):
    comment = await comment_usecase.get_comment(comment_id)

    if comment is None:
        return CustomJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            message='comment not found'
        )

    for key, value in comment_update.model_dump().items():
        if value:
            comment.__setattr__(key, value)

    result = await comment_usecase.update_comment(comment)
    return CustomJSONResponse(
        status_code=status.HTTP_200_OK,
        data=result
    )