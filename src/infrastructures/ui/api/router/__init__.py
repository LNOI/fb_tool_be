from fastapi import APIRouter

from src.infrastructures.ui.api.router import health_check,user_router,group_router,post_router, comment_router

router  = APIRouter()
router.include_router(health_check.router)
router.include_router(user_router.router,prefix='/user')
router.include_router(group_router.router,prefix='/group')
router.include_router(post_router.router,prefix='/post')
router.include_router(comment_router.router,prefix='/comment')