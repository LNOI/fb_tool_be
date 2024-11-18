from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Security
from sqlmodel import select
from starlette import status

from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.common.paginate import paginate
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import hc_usecase, group_usecase

router = APIRouter()

@router.get(
    "/",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def list_hc(user_id: UUID, page: int = 1, page_size: int = 25):
    query = select(HistoryScrapeModel).where(HistoryScrapeModel.user_id == user_id).offset((page - 1) * page_size).limit(page_size).order_by(HistoryScrapeModel.created_at.desc())
    result = await hc_usecase.query_histories(filter_query=query)
    # a_item = await  hc_usecase.get_history(UUID("f8bb029b-db3b-4582-9b3d-8b47cf521bc5"))
    result = paginate(
        items=result,
        page=page,
        page_size=page_size,
    )
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)