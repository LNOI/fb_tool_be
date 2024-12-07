from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.callbacks.manager import get_openai_callback
from dotenv import load_dotenv

load_dotenv()
import json

llm = ChatOpenAI(
    model="gpt-4o-mini",
)

prompt = """Tạo một tin nhắn chào hỏi và tư vấn khách hàng trên Facebook dựa trên thông tin sau:
-Tên khách hàng: {owner_name}
-Nội dung bài đăng của khách hàng: {title}
-Thông tin cửa hàng hoặc dịch vụ muốn quảng cáo: Cửa hàng thời trang SecondHand Chi Nhánh 2.
Hãy tuân thủ các nguyên tắc sau khi tạo nội dung tin nhắn:
-Lời chào mở đầu thân thiện, chuyên nghiệp
-Giới thiệu ngắn gọn về cửa hàng, dịch vụ của mình
-Thể hiện sự quan tâm đến nhu cầu của khách hàng dựa trên nội dung bài đăng
-Đưa ra lời mời tư vấn, hỗ trợ cụ thể cho khách hàng
-Cám ơn và kết thúc tin nhắn một cách lịch sự, để lại ấn tượng tốt
-Độ dài tin nhắn khoảng 30-50 từ
Sử dụng ngôn ngữ đơn giản, dễ hiểu trong tiếng Việt.
"""

prompt_message_category = """Tạo một tin nhắn chào hỏi và tư vấn khách hàng dựa trên nội dung của {category} trên Facebook dựa trên thông tin sau:
-Tên khách hàng: {owner_name}
-Nội dung {category} của khách hàng: {content}
-Thông tin cửa hàng hoặc dịch vụ muốn quảng cáo: Cửa hàng thời trang SecondHand Chi Nhánh 2.
Hãy tuân thủ các nguyên tắc sau khi tạo nội dung tin nhắn:
-Lời chào mở đầu thân thiện, chuyên nghiệp
-Giới thiệu ngắn gọn về cửa hàng, dịch vụ của mình
-Thể hiện sự quan tâm đến nhu cầu của khách hàng dựa trên nội dung {category}
-Đưa ra lời mời tư vấn, hỗ trợ cụ thể cho khách hàng
-Cám ơn và kết thúc tin nhắn một cách lịch sự, để lại ấn tượng tốt
-Độ dài tin nhắn khoảng 30-50 từ có thể chứa icon.
Sử dụng ngôn ngữ đơn giản, dễ hiểu trong tiếng Việt.
"""

prompt_category = """
        Hãy phân tích danh sách các {category} dưới đây và xác định xem mỗi {category} thuộc về người cần mua hay người cần bán trong bài viết sau:
        Nội dung của bài viết như sau:
        ```{post_data}```
        
        -Nội dung của bình luận dưới bài viết để phâ n tích như sau:
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

prompt_template = PromptTemplate(
    template=prompt,
    variables=["owner_name", "title"],
)

prompt_template_category = PromptTemplate(
    template=prompt_category,
    variables=["data", "category"],
)

prompt_template_message_category = PromptTemplate(
    template=prompt_message_category, variables=["owner_name", "title", "category"]
)

import time


def log_time(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

    return wrapper


import asyncio
from pprint import pprint


@log_time
async def generate_messages(inputs):
    with get_openai_callback() as callback:
        chain = prompt_template | llm | StrOutputParser()
        result = await chain.abatch(inputs=inputs, max_concurrency=1)
    print(result)
    print(callback)


@log_time
async def generate_category(inputs):
    with get_openai_callback() as callback:
        chain = prompt_template_category | llm | StrOutputParser()
        result = await chain.ainvoke(
            {
                "data": inputs,
                "post_data": "Sẵn Pedi giá tốttt",
                "category": "Các bình luận",
            }
        )
    print(result)
    print(callback)


@log_time
async def generate_message_category(inputs):
    with get_openai_callback() as callback:
        chain = prompt_template_message_category | llm | StrOutputParser()
        result = await chain.abatch(inputs=inputs, max_concurrency=10)
    print(result)
    print(callback)


if __name__ == "__main__":
    with open("./data_cmd.json", "r") as f:
        data = json.load(f)["data"]

        handled_data = [row["content"] for row in data]
        print(handled_data)
        # inputs = [
        #     {
        #         "owner_name": d["owner_name"],
        #         "content": d["content"],
        #         "category": "bình luận"
        #     }
        #     for d in data
        # ]
        # asyncio.run(generate_message_category(inputs))
        asyncio.run(generate_category(handled_data))
