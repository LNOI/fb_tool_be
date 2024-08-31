from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from src.db.posts import PostFacebook
from src.db.users import Users
from src.db.groups import GroupFacebook
from src.db.comments import CommentFacebook
from src.utils.db import get_session, Session
from sqlmodel import select

router = APIRouter(
    prefix="/user/{user_id}/groups/{group_id}/posts",
    tags=["posts"],
)

user_root_id: UUID = "00000000-0000-0000-0000-000000000000"


class CommentPost(BaseModel):
    content: str | None = None
    sender_name: str | None = None
    sender_link: str | None = None


class InputPost(BaseModel):
    title: str | None = None
    link_images: list | None = []
    video: str | None = None
    uuid_post: str | None = None
    post_date: str | None = None
    owner_name: str | None = None
    owner_link: str | None = None
    reaction: str | None = None
    comments: list[CommentPost] | None = []


# class DataInputPost(BaseModel):
#     data: list[InputPost] | None = None


@router.post("/", status_code=201)
async def create_post(
    user_id: UUID,
    group_id: UUID,
    input: InputPost,
    db: Session = Depends(get_session),
):
    """
    Create post
    """

    user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    group = db.scalars(
        select(GroupFacebook).where(GroupFacebook.id == group_id)
    ).one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    if not input.uuid_post:  # check if link_post is empty
        raise HTTPException(status_code=400, detail="uuid post is required")

    post_exist = db.scalars(
        select(PostFacebook).where(
            PostFacebook.link_post == group.link + "posts/" + input.uuid_post
        )
    ).one_or_none()
    post_dict = input.model_dump()
    comments = post_dict.pop("comments")
    if post_exist:
        for cm in comments:
            try:
                print("add comment")
                db_cm = CommentFacebook(
                    content=cm["content"],
                    post_id=post_exist.id,
                    user_id=user_id,
                    sender_name=cm["sender_name"],
                    sender_link=cm["sender_link"],
                    last_sync=datetime.now(),
                )
                db.add(db_cm)
                db.commit()
            except Exception as e:
                print(e)
        return {"message": "Post exist"}

    new_post = PostFacebook(
        **post_dict,
        link_post=group.link + "posts/" + input.uuid_post,
        user_id=user_id,
        group_id=group_id,
        last_sync=datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    for cm in comments:
        try:
            print("add comment")
            db_cm = CommentFacebook(
                content=cm["content"],
                post_id=new_post.id,
                user_id=user_id,
                sender_name=cm["sender_name"],
                sender_link=cm["sender_link"],
                last_sync=datetime.now(),
            )
            db.add(db_cm)
            db.commit()
        except Exception as e:
            print(e)

    return {"message": "Add post success"}


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


@router.get("/{post_id}")
async def get_post(
    user_id: UUID, group_id: UUID, post_id: UUID, db: Session = Depends(get_session)
):
    """
    Get post and comments
    """
    post = db.scalars(
        select(PostFacebook).where(
            PostFacebook.id == post_id,
            PostFacebook.user_id == user_id,
            PostFacebook.group_id == group_id,
        )
    ).one_or_none()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = {"post": post, "comments": []}
    comments = db.scalars(
        select(CommentFacebook).where(
            CommentFacebook.post_id == post_id, CommentFacebook.user_id == user_id
        )
    ).all()
    data["comments"] = comments
    return data
