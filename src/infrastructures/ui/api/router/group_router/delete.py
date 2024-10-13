from uuid import UUID
from fastapi import APIRouter
from starlette import status
from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import group_usecase

router = APIRouter()

@router.delete('/{group_id}', response_model=ResponseModel)
async def delete_group(group_id: UUID):
    is_deleted = await group_usecase.delete_group(group_id)
    if not is_deleted:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND, data=False)
    return CustomJSONResponse(
        status_code=status.HTTP_201_CREATED,
        data=True
    )