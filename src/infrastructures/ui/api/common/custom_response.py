import json
from datetime import date, datetime
from email.policy import default
from typing import Any, Dict, Generic, Optional, TypeVar

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from starlette import status

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    data: Optional[T] = Field(None, description="Data of the response")
    message: Optional[str] = Field(None, description="Additional information message")


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


class CustomJSONResponse(JSONResponse):
    def __init__(
        self,
        status_code: int = status.HTTP_200_OK,
        data: Any = None,
        message: Optional[str] = None,
    ) -> None:
        content = ResponseModel(
            data=data,
            message=message if message else None,
        ).model_dump(exclude_none=True)
        super().__init__(content=jsonable_encoder(content), status_code=status_code)


def success_response(
    message: str = "success", data: Any = None, status_code: int = status.HTTP_200_OK
) -> CustomJSONResponse:
    """
    Create a standardized success response.

    Args:
        message (str, optional): A success message. Defaults to "success".
        data (Any, optional): The response data. Defaults to None.
        status_code (int, optional): The HTTP status code. Defaults to 200.

    Returns:
        CustomJSONResponse: A response object with success status, message, and data.
    """

    return CustomJSONResponse(status_code=status_code, data=data, message=message)


def error_response(
    message: str = "error",
    data: Any = None,
    status_code: int = status.HTTP_400_BAD_REQUEST,
) -> CustomJSONResponse:
    """
    Create a standardized error response.

    Args:
        message (str, optional): An error message. Defaults to "error".
        data (Any, optional): Additional error data. Defaults to None.
        status_code (int, optional): The HTTP status code. Defaults to 400.

    Returns:
        CustomJSONResponse: A response object with error status, message, and data.
    """

    return CustomJSONResponse(status_code=status_code, data=data, message=message)
