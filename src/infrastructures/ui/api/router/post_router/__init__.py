from fastapi import APIRouter
from fastapi.params import Security

from src.infrastructures.ui.api.router.post_router import (
    create,
    delete,
    get,
    list,
    update,
)

router = APIRouter(
    tags=["Post"]
)
router.include_router(create.router)
router.include_router(get.router)
router.include_router(update.router)
router.include_router(delete.router)
router.include_router(list.router)
