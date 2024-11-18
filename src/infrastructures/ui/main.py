from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware
from src.infrastructures.ui.api import router


class App:
    def __init__(self):
        self._app = FastAPI()
        self.add_middleware()
        self.add_router()

    def add_middleware(self):
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],

        )

    def add_router(self):
        self._app.include_router(router.router, prefix="/api/v1")

    def get_app(self):
        return self._app


app = App().get_app()
