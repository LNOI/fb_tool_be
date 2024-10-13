from functools import wraps
from uuid import UUID
from datetime import datetime,timezone

from src.domain.model.base_model import BaseModel
from src.infrastructures.settings import config

from sqlmodel import Session, create_engine, select, SQLModel
from sqlmodel.sql._expression_select_cls import  Select

from typing import TypeVar, List, Dict,Any
from src.domain.repository.db_repository import DBRepository

engine = create_engine(config.DATABASE_URL, echo=False) if config.SERVER == "PRD" else None

T = TypeVar('T',bound=BaseModel)

def wrapper_session(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        with Session(engine) as session:
            result =  await func(*args,session,**kwargs)
            return result
    return wrapper


class FacebookDBRepository(DBRepository):
    @wrapper_session
    async def insert_item(self, item: T, session : Session) -> T:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    @wrapper_session
    async def insert_items(self, items: List[T], session : Session) -> List[T]:
        session.add_all(items)
        session.commit()
        session.refresh(items)
        return items

    @wrapper_session
    async def delete_item(self, model: T, uuid: UUID, session: Session) -> bool:
        record: T = session.scalars(select(model).where(model.id == uuid,model.deleted_at.is_(None))).one_or_none()
        if record:
            record.deleted_at = datetime.now(timezone.utc)
            session.add(record)
            session.commit()
            return True
        return False

    @wrapper_session
    async def update_item(self, item: T, session: Session) -> T:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    @wrapper_session
    async def get_item(self, model : T,uuid:UUID, session: Session) -> T:
        query = select(model).where(model.id == uuid).where(model.deleted_at.is_(None))
        return session.scalars(query).one_or_none()

    @wrapper_session
    async def query_item(self , filter_query: Select, session: Session = None) -> List[T]:
        return session.scalars(filter_query).all()

