from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from src.db.posts import PostFacebook
from src.db.users import Users
from src.db.groups import GroupFacebook
from src.utils.db import get_session, Session
from sqlmodel import select

router = APIRouter(
    prefix="/user/{user_id}/groups/{group_id}/posts",
    tags=["posts"],
)

user_root_id: UUID = "00000000-0000-0000-0000-000000000000"


class InputPost(BaseModel):
    title: str | None = None
    images: str | None = None
    video: str | None = None
    link: str | None = None
    post_date: str | None = None
    owner_name: str | None = None
    reaction: str | None = None
    profile_owner_post: str | None = None


class DataInputPost(BaseModel):
    data: list[InputPost] | None = None


@router.post("/")
async def create_post(
    user_id: UUID,
    group_id: UUID,
    input: DataInputPost,
    db: Session = Depends(get_session),
):
    """
    Create post
    """
    db_posts = []
    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    group = db.scalars(
        select(GroupFacebook).where(GroupFacebook.id == group_id)
    ).one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    for post in input.data:
        post_exist = db.scalars(
            select(PostFacebook).where(PostFacebook.link == post.link)
        ).one_or_none()
        if post_exist:
            continue
        new_post = PostFacebook(
            **post.model_dump(),
            user_id=user_id,
            group_id=group_id,
            last_sync=datetime.now(),
        )
        db_posts.append(new_post)
    db.add_all(db_posts)
    db.commit()
    return {"message": "Create post"}


@router.get("/")
async def get_posts(
    user_id: UUID,
    group_id: UUID,
    s: int = 0,
    limit: int = 15,
    db: Session = Depends(get_session),
):
    """
    Get posts
    """
    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    group = db.scalars(
        select(GroupFacebook).where(GroupFacebook.id == group_id)
    ).one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    posts = db.scalars(
        select(PostFacebook)
        .where(PostFacebook.user_id == user_id)
        .where(PostFacebook.group_id == group_id)
        .offset(s)
        .limit(limit)
        .order_by(PostFacebook.last_sync.desc())
    ).all()
    return posts
