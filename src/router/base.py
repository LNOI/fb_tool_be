from fastapi import APIRouter

BASE_ROUTER = APIRouter(prefix="/user/{user_id}", tags=["BASE"])
