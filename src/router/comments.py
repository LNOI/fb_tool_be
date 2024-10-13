from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import select

from src.db.comments import CommentFacebook
from src.db.groups import GroupFacebook
from src.db.posts import PostFacebook
from src.db.users import Users
from src.utils.db import Session, get_session

user_root_id: UUID = "00000000-0000-0000-0000-000000000000"

router = APIRouter(
    prefix="/user/{user_id}/groups/{group_id}/posts/{post_id}/comments",
    tags=["comments"],
)


class InputComment(BaseModel):
    content: str | None = None
    images: str | None = None
    sender_name: str | None = None
    sender_link: str | None = None
    note: str | None = None
    comment_date: str | None = None


class DataInputComment(BaseModel):
    data: list[InputComment] | None = None


@router.post("/", status_code=201)
async def create_comment(
    user_id: UUID,
    group_id: UUID,
    post_id: UUID,
    input: DataInputComment,
    db: Session = Depends(get_session),
):
    """
    Create comment
    """
    db_comments = []
    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    group = db.scalars(
        select(GroupFacebook).where(GroupFacebook.id == group_id)
    ).one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    post = db.scalars(
        select(PostFacebook).where(PostFacebook.id == post_id)
    ).one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    for comment in input.data:
        comment_exist = db.scalars(
            select(CommentFacebook).where(
                CommentFacebook.content == comment.content,
                CommentFacebook.sender_name == comment.sender_name,
                CommentFacebook.comment_date == comment.comment_date,
            )
        ).one_or_none()
        if comment_exist:
            continue
        comment = CommentFacebook(
            **comment.model_dump(),
            post_id=post.id,
            user_id=user.id,
            last_sync=datetime.now(),
        )
        db_comments.append(comment)
    db.add_all(db_comments)
    db.commit()
    return {"message": "Create comment"}


@router.get("/")
async def get_comments(
    user_id: UUID,
    group_id: UUID,
    post_id: UUID,
    s: int = 0,
    limit: int = 20,
    db: Session = Depends(get_session),
):
    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    group = db.scalars(
        select(GroupFacebook).where(GroupFacebook.id == group_id)
    ).one_or_none()
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    post = db.scalars(
        select(PostFacebook).where(PostFacebook.id == post_id)
    ).one_or_none()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    comments = db.scalars(
        select(CommentFacebook)
        .where(CommentFacebook.post_id == post_id)
        .offset(s)
        .limit(limit)
        .order_by(CommentFacebook.last_sync.desc())
    ).all()
    return comments
