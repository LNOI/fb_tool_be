from email.policy import default
from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.domain.model.comment_model import CommentModel
from src.domain.model.group_model import GroupModel
from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.domain.model.post_model import PostModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
import requests
from src.application.dto.history_scape_dto.history_scape_request_dto import CreateHistoryScrapeRequestDto
from src.infrastructures.ui.api.router.auth_router.login import validate_user
from src.middleware import hc_usecase, post_usecase, comment_usecase, group_usecase
import threading
router = APIRouter()

def post_request(data):
    requests.post("http://localhost:8005/api/scraper", json=data)

@router.post(
    "/",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["history scrape"])],
)
async def create_history_scrape(user_id: UUID, history_scrape: CreateHistoryScrapeRequestDto):
    item = HistoryScrapeModel(user_id=user_id, keyword=history_scrape.keyword)
    result = await hc_usecase.create_history(item)
    req = history_scrape.model_dump()
    req["hc_id"] = str(result.id)
    req["user_id"] = str(user_id)
    threading.Thread(target=post_request, args=(req,)).start()
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=result)

from pydantic import BaseModel,Field

class CommentScrapeDataDto(BaseModel):
    content : str | None = None
    owner_name : str
    owner_link : str

class PostScrapeDataDto(BaseModel):
    user_id :  UUID
    group_id: UUID
    title: str | None = None
    link: str
    images: list[str] = Field(default=[])
    owner_name: str
    owner_link: str
    reaction: int | None = None
    comments: list[CommentScrapeDataDto] = Field(default=[])
    post_date: int | None = None


@router.post("/{hc_id}/post", response_model=ResponseModel)
async def insert_post_to_history(hc_id: UUID, dto: PostScrapeDataDto):
    item = PostModel(
        **dto.model_dump(),hc_id=hc_id
    )
    post = await post_usecase.create_post(item)
    for cm in dto.comments:
        item = CommentModel(
            user_id= dto.user_id,
            post_id = post.id,
            content = cm.content,
            owner_name = cm.owner_name,
            owner_link = cm.owner_link,
            hc_id = hc_id
        )
        await comment_usecase.create_comment(item)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=post)


class GroupScrapeDataDto(BaseModel):
    user_id :  UUID
    name: str
    link: str
    privacy: str  # Công khai | Riêng tư
    members: str  # 69K thành viên  | split  69k
    posting_frequency: str
    is_member: bool = False


@router.post("/{hc_id}/group", response_model=ResponseModel)
async def insert_group_to_history(hc_id: UUID, dto: GroupScrapeDataDto):
    item = GroupModel(
        **dto.model_dump(exclude=None), hc_id=hc_id
    )
    group = await group_usecase.create_group(item)
    print(group)
    return CustomJSONResponse(status_code=status.HTTP_201_CREATED, data=group)

