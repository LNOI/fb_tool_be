from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router.comments import router as comment_router
from src.router.groups import router as group_router
from src.router.posts import router as post_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(group_router, tags=["groups"])
app.include_router(post_router, tags=["posts"])
app.include_router(comment_router, tags=["comments"])
