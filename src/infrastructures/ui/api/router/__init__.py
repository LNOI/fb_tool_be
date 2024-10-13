from fastapi import APIRouter

from src.infrastructures.ui.api.router import (
    comment_router,
    group_router,
    health_check,
    message_router,
    post_router,
    user_router,
)

router = APIRouter()
router.include_router(health_check.router)
router.include_router(user_router.router, prefix="/user")

PREFIX_USER = "/user/{user_id}"
router.include_router(group_router.router, prefix=PREFIX_USER + "/group")
router.include_router(post_router.router, prefix=PREFIX_USER + "/post")
router.include_router(message_router.router, prefix=PREFIX_USER + "/message")
router.include_router(comment_router.router, prefix=PREFIX_USER + "/comment")
