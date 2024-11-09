from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import hc_usecase

router = APIRouter()


@router.get(
    "/{hc_id}",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def get_hc(user_id: UUID, hc_id: UUID):
    result = await hc_usecase.get_history(hc_id)
    if not result:
        return CustomJSONResponse(status_code=status.HTTP_404_NOT_FOUND, data=False)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=result)  
