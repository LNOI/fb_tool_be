from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from pydantic import BaseModel
from src.utils.db import get_session, Session
from src.db.groups import GroupFacebook
from src.db.users import Users
from src.router.base import BASE_ROUTER
from src.utils.redis import cache_api, delete_cache

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
    db_groups = []
    for group in group.data:
        group_exist = db.scalars(
            select(GroupFacebook).where(
                GroupFacebook.link == group.link, GroupFacebook.user_id == user_id
            )
        ).one_or_none()
        if group_exist:
            continue
        group = GroupFacebook(
            **group.model_dump(), user_id=user_id, last_sync=datetime.now()
        )
        db_groups.append(group)
    print(db_groups)
    db.add_all(db_groups)
    db.commit()
    delete_cache(f"get_groups-user_id_{user_id}")
    return {"message": "Create group"}


@router.get("/")
# @cache_api(ex=60)
async def get_groups(
    user_id: UUID, s: int = 0, limit: int = 15, db: Session = Depends(get_session)
):
    groups = db.scalars(
        select(GroupFacebook)
        .where(GroupFacebook.user_id == user_id, GroupFacebook.deleted.is_(False))
        .offset(s)
        .limit(limit)
        .order_by(GroupFacebook.last_sync.desc())
    ).all()

    groups = [
        {
            **group.model_dump(),
            "total_post": [post for post in group.posts if not post.deleted].__len__(),
        }
        for group in groups
    ]
    return groups


@router.delete("/{group_id}")
async def delete_group(
    user_id: UUID, group_id: UUID, db: Session = Depends(get_session)
):
    group = db.scalars(
        select(GroupFacebook).where(
            GroupFacebook.user_id == user_id, GroupFacebook.id == group_id
        )
    ).one_or_none()
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    group.deleted = True
    db.add(group)
    db.commit()
    return None


class InputGroupIdDelete(BaseModel):
    group_ids: list[UUID] | None = []


@router.post("/edit/delete")
async def edit_delete_group(
    user_id: UUID, input: InputGroupIdDelete, dp: Session = Depends(get_session)
):
    db_groups = []
    for group_id in input.group_ids:
        group = dp.scalars(
            select(GroupFacebook).where(
                GroupFacebook.user_id == user_id, GroupFacebook.id == group_id
            )
        ).one_or_none()
        if group is None:
            continue
        group.deleted = True
        db_groups.append(group)
    dp.add_all(db_groups)
    dp.commit()
    delete_cache(f"get_groups-user_id_{user_id}")
    return None
