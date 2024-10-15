from fastapi import  APIRouter

from src.infrastructures.ui.api.common.custom_response import CustomJSONResponse

router = APIRouter()

# @router.post("/token", response_model=CustomJSONResponse):
# async def set_token(current_user):
#     pass