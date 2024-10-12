# from src.config import config
# from sqlalchemy import create_engine,Engine
# from sqlmodel import Session
#
# engine : Engine = None # ignore
#
# if config.VIRTUAL_ENV == "TESTING":
#     engine = create_engine(config.DATABASE_URL_TEST, echo=False)
#
# def get_session():
#     with Session(engine) as session:
#         yield session
