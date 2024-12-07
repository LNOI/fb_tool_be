from fastapi import HTTPException, Request
from uuid import UUID
from loguru import logger

from starlette import status

from src.middleware import sessions_usecase, accounts_usecase

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def validate_session_token(
    request: Request,
) -> UUID:
    """
    Validate user from session-token cookie is a uuid4
    """
    session_token = request.cookies.get("authjs.session-token")

    if session_token is None:
        raise credentials_exception
    try:
        session = await sessions_usecase.get_session(session_token)

        if session:
            return session.userId
    except Exception as e:
        logger.error(f"Error validating user : {session_token} : {e}")
    raise credentials_exception


async def validate_session_admin_token(
    request: Request,
) -> UUID:
    """
    Validate user from session-token cookie is a uuid4
    """
    session_token = request.cookies.get("authjs.session-token")

    if session_token is None:
        raise credentials_exception
    try:
        session = await sessions_usecase.get_session(session_token)
        if session:
            return session.userId
    except Exception as e:
        logger.error(f"Error validating user : {session_token} : {e}")
    raise credentials_exception