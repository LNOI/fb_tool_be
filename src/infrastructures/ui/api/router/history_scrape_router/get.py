from uuid import UUID

from fastapi import APIRouter, Security
from starlette import status

from src.domain.model.group_model import GroupModel
from src.domain.model.post_model import PostModel
from src.infrastructures.ui.api.common.custom_response import (
    CustomJSONResponse,
    ResponseModel,
)
from sqlmodel import select

from src.application.dto.history_scape_dto.history_scape_response_dto import (
    HistoryScrapeResponseDto,
)
from src.domain.model.history_scrape_model import HistoryScrapeModel
from src.middleware import hc_usecase, group_usecase, post_usecase
from sqlalchemy.orm import selectinload

router = APIRouter()


@router.get(
    "/{hc_id}",
    response_model=ResponseModel,
    # dependencies=[Security(validate_user, scopes=["group"])],
)
async def get_hc(user_id: UUID, hc_id: UUID):
    select_query = (
        select(HistoryScrapeModel)
        .options(
            selectinload(HistoryScrapeModel.groups).options(
                selectinload(GroupModel.posts).options(selectinload(PostModel.comments))
            )
        )
        .where(HistoryScrapeModel.user_id == user_id, HistoryScrapeModel.id == hc_id)
    )

    result = await hc_usecase.query_histories(filter_query=select_query)

    resp = HistoryScrapeResponseDto(**result[0].model_dump(exclude=None))

    for group in result[0].groups:
        data_g = group.model_dump()
        data_g["posts"] = []
        for post in group.posts:
            data_p = post.model_dump()
            data_p["comments"] = []
            for comment in post.comments:
                data_p["comments"].append(comment.model_dump())
            data_g["posts"].append(data_p)
        resp.groups.append(data_g)
    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=resp)
