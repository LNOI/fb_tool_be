from uuid import UUID

from fastapi import APIRouter
from sqlmodel import select
from starlette import status
import threading

from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)


router = APIRouter()
import requests


def request_send_message_auto():
    requests.post("http://localhost:8005/api/send_message")


@router.post("/", response_model=ResponseModel)
async def send_message(user_id: UUID):
    # sandbox testing code

    threading.Thread(target=request_send_message_auto, args=()).start()

    return CustomJSONResponse(status_code=status.HTTP_200_OK)
