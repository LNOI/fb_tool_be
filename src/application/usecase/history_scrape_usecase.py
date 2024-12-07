from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.domain.service.history_scrape_service import HistoryScrapeService


class HistoryScrapeUseCase:
    @inject
    def __init__(self, hc_service: HistoryScrapeService):
        self._hc_service: HistoryScrapeService = hc_service

    async def create_history(self, hc: HistoryScrapeModel) -> HistoryScrapeModel:
        return await self._hc_service.create_history_scrape(hc)

    async def get_history(self, id: UUID) -> HistoryScrapeModel:
        return await self._hc_service.get_history_scrape(id)

    async def update_history(self, hc: HistoryScrapeModel) -> HistoryScrapeModel:
        return await self._hc_service.update_history_scrape(hc)

    async def delete_history(self, id: UUID) -> HistoryScrapeModel:
        return await self._hc_service.delete_history_scrape(id)

    async def query_history(self, filter_query: Select):
        return await self._hc_service.query_history_scrape(filter_query)

    async def query_histories(self, filter_query: Select):
        return await self._hc_service.query_history_scrapes(filter_query)
