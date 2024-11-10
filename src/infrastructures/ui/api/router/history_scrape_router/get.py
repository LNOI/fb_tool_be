from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from sqlmodel import select

from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.application.dto.history_scape_dto.history_scape_response_dto import HistoryScrapeResponseDto
from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.middleware import hc_usecase, group_usecase, post_usecase
from sqlalchemy.orm import selectinload

router = APIRouter()


@router.get(
    "/{hc_id}",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def get_hc(user_id: UUID, hc_id: UUID):
    select_query = select(HistoryScrapeModel).options(
            selectinload(HistoryScrapeModel.list_group)
        ).options(
            selectinload(HistoryScrapeModel.list_post)
        ).where(HistoryScrapeModel.user_id == user_id, HistoryScrapeModel.id == hc_id)
    result = await hc_usecase.query_histories(filter_query=select_query)
    
    resp = HistoryScrapeResponseDto(**result[0].model_dump(exclude=None))
    resp.list_group = [ group for group in result[0].list_group]
    resp.list_post = [ post for post in result[0].list_post]    
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=resp)  
