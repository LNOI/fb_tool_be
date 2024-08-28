from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from pydantic import BaseModel
from src.utils.db import get_session, Session
from src.db.groups import GroupFacebook
from src.db.users import Users
from src.router.base import BASE_ROUTER

user_root_id: UUID = "00000000-0000-0000-0000-000000000000"

router = APIRouter(
    prefix="/user/{user_id}/groups",
    tags=["groups"],
)


class InputGroup(BaseModel):
    link: str
    name: str
    description: str | None = None
    privacy: str
    members: str
    post_per_day: str | None = "0"
    user_admin: str | None = None


class DataInputGroup(BaseModel):
    data: list[InputGroup] | None = None


@router.post("/", status_code=201)
async def create_group(
    user_id: UUID, group: DataInputGroup, db: Session = Depends(get_session)
):
    print(user_id)
    db_groups = []
    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for group in group.data:
        group_exist = db.scalars(
            select(GroupFacebook).where(GroupFacebook.link == group.link)
        ).one_or_none()
        if group_exist:
            continue
        group = GroupFacebook(
            **group.model_dump(), user_id=user.id, last_sync=datetime.now()
        )
        db_groups.append(group)
    print(db_groups)
    db.add_all(db_groups)
    db.commit()
    return {"message": "Create group"}


@router.get("/")
async def get_groups(
    user_id: UUID, s: int = 0, limit: int = 15, db: Session = Depends(get_session)
):
    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    groups = db.scalars(
        select(GroupFacebook)
        .where(GroupFacebook.user_id == user.id)
        .offset(s)
        .limit(limit)
        .order_by(GroupFacebook.last_sync.desc())
    ).all()
    return groups