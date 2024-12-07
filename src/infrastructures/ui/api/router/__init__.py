from fastapi import APIRouter

from src.infrastructures.ui.api.router import (
    comment_router,
    group_router,
    health_check,
    message_router,
    post_router,
    history_scrape_router,
    llm_router,
)

router = APIRouter()
router.include_router(health_check.router)
# router.include_router(user_router.router, prefix="/user")

router.include_router(group_router.router, prefix="/group")
router.include_router(post_router.router, prefix="/post")
router.include_router(message_router.router, prefix="/message")
router.include_router(comment_router.router, prefix="/comment")
router.include_router(history_scrape_router.router, prefix="/history-scrape")
router.include_router(llm_router.router, prefix="/llm")
