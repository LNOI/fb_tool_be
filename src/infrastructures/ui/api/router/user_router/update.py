from uuid import  UUID
from fastapi import APIRouter
from starlette import status

from src.application.dto.user_dto.user_request_dto import UpdateUserRequestDto
from src.domain.model.user_model import UserModel
from src.infrastructures.ui.api.common.custom_response import ResponseModel, CustomJSONResponse
from src.middleware import user_usecase

router = APIRouter()

@router.put('/{user_id}', response_model=ResponseModel)
async def update_user(user_id : UUID,  user_update: UpdateUserRequestDto):
    user = await user_usecase.get_user(user_id)

    if user is None:
        return CustomJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            message='User not found'
        )

    for key, value in user_update.model_dump().items():
        if value:
            user.__setattr__(key, value)

    result = await user_usecase.update_user(user)
    return CustomJSONResponse(
        status_code=status.HTTP_200_OK,
        data=result
    )