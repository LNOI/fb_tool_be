from fastapi import APIRouter

from src.infrastructures.ui.api.router import health_check,user_router

router  = APIRouter()
router.include_router(health_check.router)
router.include_router(user_router.router,prefix='/user')