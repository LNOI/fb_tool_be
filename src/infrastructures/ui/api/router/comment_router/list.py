from fastapi import APIRouter
from sqlmodel import select
from starlette import status

from src.domain.model.comment_model import CommentModel
from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import comment_usecase
from src.infrastructures.ui.api.common.paginate import paginate
router = APIRouter()

@router.get('/', response_model = ResponseModel)
async def list_comment(page:int =1,page_size : int = 25):
    query = select(CommentModel).limit(page_size).offset((page-1)*page_size).order_by(CommentModel.created_at.desc())
    result = await comment_usecase.query_comment(filter_query=query)

    result = paginate(
        items=result,
        page=page,
        page_size=page_size,
    )
    return CustomJSONResponse(
        status_code=status.HTTP_200_OK,
        data=result
    )