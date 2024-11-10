from fastapi import APIRouter

from src.infrastructures.ui.api.router.history_scrape_router import (
    create,
    get,
    update,
    list,   
)

router = APIRouter(tags=["History Scrape Router"])
router.include_router(create.router)
router.include_router(get.router)
router.include_router(update.router)
# router.include_router(delete.router)
router.include_router(list.router)
