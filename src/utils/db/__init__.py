from sqlalchemy import create_engine
from sqlmodel import Session

from src.config import config

engine = create_engine(config.DATABASE_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session
