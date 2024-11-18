from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.application.dto.group_dto.group_request_dto import CreateGroupRequestDto
from src.domain.model.group_model import GroupModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from sqlmodel import select
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import group_usecase

router = APIRouter()


@router.post(
    "/",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def create_group(user_id: UUID, group: CreateGroupRequestDto):
    item: GroupModel = GroupModel(**group.model_dump(), user_id=user_id)
    result = await group_usecase.create_group(item)

    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
