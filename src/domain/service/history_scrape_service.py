from typing import  List
from uuid import UUID

from injector import inject
from sqlmodel.sql._expression_select_cls import Select

from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.domain.repository.db_repository import DBRepository


class HistoryScrapeService:

    @inject
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    async def create_history_scrape(self, hc: HistoryScrapeModel) -> HistoryScrapeModel:
        return await self.db_repository.insert_item(hc)

    async def get_history_scrape(self, id: UUID) -> HistoryScrapeModel:
        return await self.db_repository.get_item(HistoryScrapeModel, id)

    async def update_history_scrape(self, hc: HistoryScrapeModel) -> HistoryScrapeModel:
        return await self.db_repository.update_item(hc)

    async def delete_history_scrape(self, id: UUID) -> bool:
        return await self.db_repository.delete_item(HistoryScrapeModel, id)

    async def query_history_scrape(self, filter_query: Select) -> List[HistoryScrapeModel]:
        return await self.db_repository.query_item(filter_query)

    async def query_history_scrapes(self, filter_query: Select) -> List[HistoryScrapeModel]:
        return await self.db_repository.query_items(filter_query)
