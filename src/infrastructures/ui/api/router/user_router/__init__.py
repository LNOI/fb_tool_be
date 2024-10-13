from fastapi import APIRouter

from src.infrastructures.ui.api.router.user_router import (
    create,
    delete,
    get,
    list,
    update,
)

router = APIRouter(tags=["Users"])
router.include_router(create.router)
router.include_router(get.router)
router.include_router(update.router)
router.include_router(delete.router)
router.include_router(list.router)
