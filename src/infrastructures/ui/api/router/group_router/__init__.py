from fastapi import APIRouter
from src.infrastructures.ui.api.router.group_router import  create,get, update,delete, list

router = APIRouter(tags=["Group Router"])
router.include_router(create.router)
router.include_router(get.router)
router.include_router(update.router)
router.include_router(delete.router)
router.include_router(list.router)