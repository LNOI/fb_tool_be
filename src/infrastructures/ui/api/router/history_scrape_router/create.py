from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import hc_usecase

router = APIRouter()


@router.post(
    "/",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["history scrape"])],
)
async def create_history_scrape(user_id: UUID):
    item = HistoryScrapeModel(user_id=user_id)
    result = await hc_usecase.create_history(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)
    
    
    
