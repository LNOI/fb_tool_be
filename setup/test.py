from typing import Optional

from pydantic import BaseModel


class op(BaseModel):
    post_id: str
    user_id: str
    content: Optional[str] = None
    images: list[str] = []
    sender_name: Optional[str] = None
    sender_link: Optional[str] = None
    note: Optional[str] = None
    comment_date: Optional[float] = None


print(
    op(
        post_id="1",
        user_id="1",
    )
)
