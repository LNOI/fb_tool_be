from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from src.application.dto.group_dto.group_request_dto import CreateGroupRequestDto, CreateGroupRequestAdminDto
from src.domain.model.group_model import GroupModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.utils.auth import validate_session_token
from src.middleware import group_usecase

router = APIRouter()


@router.post(
    "/",
    response_model=ResponseModel,
)
async def create_group( group: CreateGroupRequestDto,user_id: UUID = Depends(validate_session_token)):
    item: GroupModel = GroupModel(**group.model_dump(), user_id=user_id)
    result = await group_usecase.create_group(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)


# add for admin
@router.post("/admin", response_model=ResponseModel)
async def create_group_admin(group: CreateGroupRequestAdminDto):
    item = GroupModel(**group.model_dump())
    result = await group_usecase.create_group(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
