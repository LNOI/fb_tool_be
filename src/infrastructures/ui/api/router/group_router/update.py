from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.application.dto.group_dto.group_request_dto import UpdateGroupRequestDto
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import group_usecase

router = APIRouter()


@router.put(
    "/{group_id}",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def update_group(
    user_id: UUID, group_id: UUID, group_update: UpdateGroupRequestDto
):
    group = await group_usecase.get_group(group_id)

    if group is None:
        return CustomJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, message="User not found"
        )

    for key, value in group_update.model_dump().items():
        if value:
            group.__setattr__(key, value)

    result = await group_usecase.update_group(group)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
