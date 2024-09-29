from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from src.db.posts import PostFacebook
from src.db.users import Users
from src.db.groups import GroupFacebook
from src.db.comments import CommentFacebook
from src.utils.db import get_session, Session
from src.utils.redis import cache_api, delete_cache
from sqlmodel import select
from typing import Annotated, Union

router = APIRouter(
    prefix="/user/{user_id}",
    tags=["posts"],
)


class CommentPost(BaseModel):
    content: str | None = None
    sender_name: str | None = None
    sender_link: str | None = None


class InputPost(BaseModel):
    group_id: UUID | None = None
    title: str | None = None
    link_images: list | None = []
    video: str | None = None
    link_post: str
    post_date: str | None = None
    owner_name: str | None = None
    owner_link: str | None = None
    reaction: str | None = None
    comments: list[CommentPost] | None = []


class InputPostIdDelete(BaseModel):
    post_ids: list[UUID] | None = []


@router.post("/posts", status_code=201)
async def create_post(
    user_id: UUID,
    input: InputPost,
    db: Session = Depends(get_session),
):
    """
    Create post
    """

    if input.group_id:
        group = db.scalars(
            select(GroupFacebook).where(GroupFacebook.id == input.group_id)
        ).one_or_none()
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")

    if not input.link_post:  # check if link_post is empty
        raise HTTPException(status_code=400, detail="Link post is required")

    post_exist = db.scalars(
        select(PostFacebook).where(PostFacebook.link_post == input.link_post)
    ).one_or_none()
    post_dict = input.model_dump()
    comments = post_dict.pop("comments")
    reaction = int(post_dict.pop("reaction"))
    if post_exist:
        post_exist.owner_name = post_dict["owner_name"]
        post_exist.owner_link = post_dict["owner_link"]
        post_exist.link_images = post_dict["link_images"]
        post_exist.title = post_dict["title"]
        post_exist.last_sync = datetime.now()
        post_exist.number_of_reaction = reaction
        db.add(post_exist)
        db.commit()
        for cm in comments:
            try:
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
        print(input.link_post)
        return {"message": "Post exist"}

    new_post = PostFacebook(
        **post_dict,
        user_id=user_id,
        last_sync=datetime.now(),
        number_of_reaction=reaction,
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


@router.get("/posts")
async def get_posts(
    user_id: Annotated[UUID, "the uuid"],
    group_id: Annotated[Union[UUID, None], "ID group of POST"] = None,
    page: int = 0,
    limit: int = 25,
    db: Session = Depends(get_session),
):
    """
    API used by get post with condition
    """
    query = select(PostFacebook).where(PostFacebook.user_id == user_id)
    if group_id:
        query = query.where(PostFacebook.group_id == group_id)
    return db.scalars(
        query.offset(page * limit).limit(limit).order_by(PostFacebook.last_sync.desc())
    ).all()


@router.get("/posts/{id}")
async def get_post( user_id: Annotated[UUID, "the uuid"],id: UUID,
    group_id: Annotated[Union[UUID, None], "ID group of POST"] = None,
    db: Session = Depends(get_session)
    ):
    query = select(PostFacebook).where(PostFacebook.user_id==user_id, PostFacebook.id == id)
    if group_id:
        query = query.where(PostFacebook.group_id== group_id)
    return db.scalars(query).one_or_none()
    

@router.delete("/posts/edit/delete")
async def edit_delete_post_id(
    user_id: UUID,
    input: InputPostIdDelete,
    db: Session = Depends(get_session),
):
    db_posts = []

    for post_id in input.post_ids:
        post = db.scalars(
            select(PostFacebook).where(
                PostFacebook.user_id == user_id,
                PostFacebook.id == post_id,
            )
        ).one_or_none()
        if post is None:
            continue
        post.deleted = True
        db_posts.append(post)
    db.add_all(db_posts)
    db.commit()

    return {"message": "Delete post success"}
