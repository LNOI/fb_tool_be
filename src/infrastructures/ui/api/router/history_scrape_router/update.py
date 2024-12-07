from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.application.dto.history_scape_dto.history_scape_request_dto import (
    UpdateHistoryScrapeRequestDto,
)
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.middleware import hc_usecase

router = APIRouter()


@router.put(
    "/{hc_id}",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def update_hc(
    user_id: UUID, hc_id: UUID, history_scrape: UpdateHistoryScrapeRequestDto
):
    hc = await hc_usecase.get_history(hc_id)
    if hc is None:
        return CustomJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, message="History Scrape not found"
        )

    for key, value in history_scrape.model_dump().items():
        if value:
            hc.__setattr__(key, value)

    result = await hc_usecase.update_history(hc)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)
