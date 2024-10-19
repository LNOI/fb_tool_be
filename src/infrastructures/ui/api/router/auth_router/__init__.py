from fastapi import APIRouter

from src.infrastructures.ui.api.router.auth_router import login

router = APIRouter(tags=["Authentication & Authorization"])
router.include_router(login.router)
