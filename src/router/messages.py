from uuid import uuid1, UUID
from fastapi import APIRouter, Depends
from src.db.messages import MessagesFacebook, TemplateMessage
from src.db.users import Users
from src.utils.db import get_session, Session
from sqlmodel import select
from pydantic import BaseModel


router = APIRouter(prefix="/user/{user_id}/messages", tags=["messages"])


class InputTemplateMessage(BaseModel):
    name: str
    content: str
    images: str | None = None
    tags: str | None = None


class InputMessage(BaseModel):
    content: str
    images: str
    receiver_user_name: str
    receiver_user_profile: str
    tags: str | None = None
    template_id: UUID | None = None


@router.post("/", status_code=201)
async def create_message(
    user_id: UUID, input: InputMessage, db: Session = Depends(get_session)
):
    """
    Create message
    """
    # user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()

    # if not user:
    #     return {"message": "User not found"}

    message = MessagesFacebook(**input.model_dump(), user_id=user_id)
    db.add(message)
    db.commit()
    return {"message": "Create message"}


@router.get("/")
async def get_messages(user_id: str, db: Session = Depends(get_session)):
    """
    get all messages
    """
    # user = db.scalars(select(Users).where(Users.id == user_id)).one_or_none()

    # if not user:
    #     return {"message": "User not found"}

    messages = db.exec(
        select(MessagesFacebook)
        .where(MessagesFacebook.user_id == user_id)
        .order_by(MessagesFacebook.created_at.desc())
    ).all()
    return messages


@router.post("/template")
async def create_template_message(
    user_id: str, input: InputTemplateMessage, db: Session = Depends(get_session)
):
    """
    Create template message
    """
    t = TemplateMessage(**input.model_dump(), user_id=user_id)
    db.add(t)
    db.commit()
    return {"message": "Create template message"}


@router.get("/template")
async def get_template_messages(user_id: str, db: Session = Depends(get_session)):
    """
    get all template messages
    """
    return db.exec(
        select(TemplateMessage).where(TemplateMessage.user_id == user_id)
    ).all()
