from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://fbtool:password@localhost:5445/fbtool_db"


config = Settings()
