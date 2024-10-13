from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVER: str = "PRD"
    DATABASE_URL: str = "postgresql+psycopg2://fbtool:password@localhost:5445/fbtool_db"
    DATABASE_TEST_URL: str = (
        "postgresql+psycopg2://fbtool:password@localhost:5445/fbtool_db_test"
    )


config = Settings()
