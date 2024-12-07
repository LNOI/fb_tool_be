import json
from fastapi import APIRouter
from uuid import UUID
from starlette import status
from src.domain.model.comment_model import CommentModel
from src.domain.model.post_model import PostModel
from src.infrastructures.ui.api.common.custom_response import CustomJSONResponse
from src.middleware import comment_usecase, post_usecase
from sqlmodel import select
from sqlalchemy.orm import selectinload


router = APIRouter()
from pydantic import BaseModel
from enum import Enum
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.callbacks.manager import get_openai_callback
from src.infrastructures.settings import config


class TypeGenMessage(str, Enum):
    POST = "POST"
    COMMENT = "COMMENT"


class GenRequestDto(BaseModel):
    type: TypeGenMessage


@router.post("/{hc_id}")
async def generate_message(user_id: UUID, hc_id: UUID, dto: GenRequestDto):
    query = select(CommentModel).where(
        CommentModel.hc_id == hc_id, CommentModel.user_id == user_id
    )
    comments = await comment_usecase.query_comments(query)

    return CustomJSONResponse(status_code=status.HTTP_200_OK, data=comments)


@router.post("/{hc_id}/category")
async def generate_message(user_id: UUID, hc_id: UUID, dto: GenRequestDto):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=config.OPENAI_API_KEY)
    prompt_category_post = """
            Hãy phân tích danh sách các nội dung các bài viết dưới đây và xác định xem mỗi bài viết thuộc về người cần mua hay người cần bán trong bài viết sau:
            Nội dung danh sách các bài viết như sau:
            ```{data_post}```

            Các tiêu chí để phân loại:
            -Nếu bài viết thể hiện nhu cầu mua hàng, tìm kiếm sản phẩm hoặc dịch vụ, hỏi về giá cả, chất lượng, địa điểm bán, vận chuyển, v.v., hãy xếp vào nhóm "người cần mua".
            -Nếu bài viết thể hiện ý định bán hàng, quảng cáo sản phẩm, dịch vụ, cung cấp thông tin chi tiết về hàng hóa, giá cả, khuyến mãi, liên hệ mua hàng v.v., hãy xếp vào nhóm "người cần bán".
            -Nếu bài viết chỉ chứa các các từ khoá nghĩa liên quan đến nhắn tin cho tôi thì hãy xếp vào nhóm "người cần bán".
            -Nếu bài viết không rõ ràng hoặc không chứa thông tin liên quan đến mua/bán, hãy xếp vào nhóm "không xác định".
            -Nếu bài viết có các từ ib, inbox, liên hệ, v.v. thì nếu bài viết là bán hàng thì xếp vào nhóm "người cần mua", ngược lại xếp vào nhóm "người cần bán"
            -Hãy đưa ra kết quả phân tích dưới dạng một danh sách "người cần mua" hoặc "người cần bán", hoặc ghi chú "không xác định" nếu không thể xác định được.
            - Sử dụng ngôn ngữ tiếng Việt để phân tích và trình bày kết quả.

            *Kết quả chỉ là 1 danh sách như bên dưới:
            Ví dụ: ["người cần mua", "người cần bán", "không xác định",...]
            """

    prompt_category_comment = """
        Hãy phân tích danh sách các bình luận từ mọi người dưới đây và xác định xem mỗi bình luận thuộc về người cần mua hay người cần bán trong bài viết sau:
        Nội dung của bài viết như sau:
        ```{data_post}```
        
        -Nội dung của bình luận dưới bài viết để phân tích như sau:
        ```{data}```
    
        Các tiêu chí để phân loại:
        -Nếu bình luận thể hiện nhu cầu mua hàng, tìm kiếm sản phẩm hoặc dịch vụ, hỏi về giá cả, chất lượng, địa điểm bán, vận chuyển, v.v., hãy xếp vào nhóm "người cần mua".
        -Nếu bình luận thể hiện ý định bán hàng, quảng cáo sản phẩm, dịch vụ, cung cấp thông tin chi tiết về hàng hóa, giá cả, khuyến mãi, liên hệ mua hàng v.v., hãy xếp vào nhóm "người cần bán".
        -Nếu bình luận chỉ chứa các các từ khoá nghĩa liên quan đến nhắn tin cho tôi thì hãy xếp vào nhóm "người cần bán".
        -Nếu bình luận không rõ ràng hoặc không chứa thông tin liên quan đến mua/bán, hãy xếp vào nhóm "không xác định".
        -Nếu bình luận có các từ ib, inbox, liên hệ, v.v. thì nếu bài viết là bán hàng thì xếp vào nhóm "người cần mua", ngược lại xếp vào nhóm "người cần bán"
        -Hãy đưa ra kết quả phân tích dưới dạng một danh sách "người cần mua" hoặc "người cần bán", hoặc ghi chú "không xác định" nếu không thể xác định được.
        - Sử dụng ngôn ngữ tiếng Việt để phân tích và trình bày kết quả.

        *Kết quả chỉ là 1 danh sách như bên dưới:
        Ví dụ: ["người cần mua", "người cần bán", "không xác định",...]
        """

    prompt_template_category_comment = PromptTemplate(
        template=prompt_category_comment,
        variables=["data_post", "data"],
    )

    prompt_template_category_post = PromptTemplate(
        template=prompt_category_post,
        variables=["data_post"],
    )

    posts = await post_usecase.query_posts(
        select(PostModel)
        .options(selectinload(PostModel.comments))
        .where(PostModel.hc_id == hc_id, PostModel.user_id == user_id)
    )

    title_posts = []

    for p in posts:
        title_posts.append(p.title)
        data = [c.content for c in p.comments]
        if data:
            with get_openai_callback() as callback:
                chain = prompt_template_category_comment | llm | StrOutputParser()
                result = await chain.ainvoke({"data": data, "data_post": p.title})
            contents = json.loads(result)
            for idx, content in enumerate(contents):
                p.comments[idx].category = content
            await comment_usecase.update_comments(p.comments)

    with get_openai_callback() as callback:
        chain = prompt_template_category_post | llm | StrOutputParser()
        result = await chain.ainvoke(
            {
                "data_post": title_posts,
            }
        )
    contents = json.loads(result)
    for idx, content in enumerate(contents):
        posts[idx].category = content
    await post_usecase.update_posts(posts)

    return CustomJSONResponse(status_code=status.HTTP_200_OK)
