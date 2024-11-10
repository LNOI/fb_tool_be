from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.application.dto.group_dto.group_request_dto import CreateGroupRequestDto
from src.domain.model.group_model import GroupModel, StatusGroupScrape
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
    dependencies=[Security(validate_user, scopes=["group"])],
)
async def create_group(user_id: UUID, group: CreateGroupRequestDto):
    query = select(GroupModel).where(GroupModel.link_group == group.link_group, GroupModel.user_id == user_id)
    group_exists = await group_usecase.query_groups(query)
    
    if group_exists:
        print(f"Group exists: {group_exists[0].link_group}")
        group_exists[0].status = StatusGroupScrape.PENDING
        group_exists[0].hc_id = group.hc_id
        
        result = await group_usecase.update_group(group_exists[0])
    else:
        item: GroupModel = GroupModel(**group.model_dump(), status=StatusGroupScrape.PENDING, user_id=user_id)
        result = await group_usecase.create_group(item)
 
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
