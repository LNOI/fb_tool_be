from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import group_usecase

router = APIRouter()


@router.get(
    "/{group_id}",
    response_model=ResponseModel,
    dependencies=[Security(validate_user, scopes=["group"])],
)
async def get_group(user_id: UUID, group_id: UUID):
    group = await group_usecase.get_group(group_id)
    if not group:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=group)
