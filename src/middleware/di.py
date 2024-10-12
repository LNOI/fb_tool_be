# Where will add import
from injector import Binder,Module

from src.domain.repository.db_repository import DBRepository
from src.infrastructures.database.postgresql.db_prd import FacebookDBRepository


class ApplicationModule(Module):
    def configure(self, binder: Binder)->None:
        binder.bind(DBRepository, to= FacebookDBRepository()) # type: ignore

class ApplicationTestModule(Module):
    def configure(self, binder: Binder)->None:
        binder.bind(DBRepository, to= FacebookDBRepository()) # type: ignore

