from fastapi import APIRouter
from src.infrastructures.ui.api.router.llm_router import generate_message


router = APIRouter(tags=["Langchain"])
router.include_router(generate_message.router)
