from injector import inject

from src.domain.model.sessions_model import SessionsModel
from src.domain.service.sessions_service import SessionsService


class SessionsUseCase:
    @inject
    def __init__(self, sessions_service: SessionsService):
        self._sessions_service: SessionsService = sessions_service

    async def get_session(self, sessionToken: str) -> SessionsModel:
        """
        Get session by sessionToken

        Args:
            sessionToken (str): sessionToken
        """
        return await self._sessions_service.get_session(sessionToken)
