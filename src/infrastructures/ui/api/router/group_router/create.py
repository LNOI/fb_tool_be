from uuid import UUID

from fastapi import APIRouter
from starlette import status

from src.application.dto.group_dto.group_request_dto import CreateGroupRequestDto
from src.domain.model.group_model import GroupModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import group_usecase

router = APIRouter()


@router.post("/", response_model=ResponseModel)
async def create_group(user_id: UUID, group: CreateGroupRequestDto):
    item: GroupModel = GroupModel(**group.model_dump())
    result = await group_usecase.create_group(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
