from uuid import UUID
from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
)


@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


user_root_id: UUID = "00000000-0000-0000-0000-000000000000"
