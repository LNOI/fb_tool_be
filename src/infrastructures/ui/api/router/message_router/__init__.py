from fastapi import APIRouter

from src.infrastructures.ui.api.router.message_router import send

router = APIRouter(tags=["Message"])
router.include_router(send.router)
# router.include_router(create.router)
# router.include_router(get.router)
# router.include_router(update.router)
# router.include_router(delete.router)
# router.include_router(list.router)
