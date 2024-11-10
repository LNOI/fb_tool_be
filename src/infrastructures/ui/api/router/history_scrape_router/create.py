from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.application.dto.history_scape_dto.history_scape_request_dto import CreateHistoryScrapeRequestDto
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import hc_usecase

router = APIRouter()


@router.post(
    "/",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["history scrape"])],
)
async def create_history_scrape(user_id: UUID, history_scrape: CreateHistoryScrapeRequestDto):
    item = HistoryScrapeModel(user_id=user_id, keyword=history_scrape.keyword)
    result = await hc_usecase.create_history(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)