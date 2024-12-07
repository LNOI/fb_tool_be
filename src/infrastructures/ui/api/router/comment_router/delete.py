from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.utils.auth import validate_session_token
from src.middleware import comment_usecase

router = APIRouter()


@router.delete("/{comment_id}", response_model=ResponseModel)
async def delete_comment(comment_id: UUID, user_id: UUID = Depends(validate_session_token)):
    is_deleted = await comment_usecase.delete_comment(comment_id, user_id)
    if not is_deleted:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND, data=False)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=True)
