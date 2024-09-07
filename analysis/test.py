import requests
import json
from datetime import datetime

# sample_group = {
#     "link": "https://www.facebook.com/groups/113194777190399/",
#     "name": "🏘🏠 Cho Thuê Phòng Trọ - Nhà Nguyên Căn - Chung Cư - Ở Ghép Tại TP.HCM",
#     "privacy": "Công khai",
#     "members": " 392K thành viên ",
#     "post_per_day": " 10+ bài viết mỗi ngày",
# }

# sample_post = {
#     "title": "Thue phong tro quan 10",
#     "link_post": "https://www.facebook.com/groups/113194777190399/",
#     "link_images": [],
#     "reaction": "100",
#     "owner_name": "thanhloi",
#     "owner_link": "https://www.facebook.com/thanhloi",
#     "comments": [
#         {
#             "content": "Tôi cần thuê",
#             "owner_link": "https://www.facebook.com/thanhloi",
#             "owner_name": "thanhloi",
#         }
#     ],
# }
# {
#     "owner_name": "Lê Hoài Lam",
#     "owner_link": "https://www.facebook.com/100047470752621",
#     "title": "Căn Studio Trống Sẵn Ban Công Cực To Tách Bếp Sau Lưng The Vista An Phú\nĐường 16 An Phú \n-nhà rộng có sẵn ban công to sân vườn \n-nội thất trang bị đầy đủ y hình … Xem thêm\n+4",
#     "reaction": "1",
#     "links_images": [],
#     "comments": [
#         {
#             "sender_name": "Khả Ngân",
#             "sender_link": "100024926827577",
#             "content": "Xin giá ạ"
#         },
#         {
#             "sender_name": "Lê Hoài Lam",
#             "sender_link": "100047470752621",
#             "content": "Cho pet"
#         }
#     ],
#     "link_post": ""
# }
# resp = requests.post(
#     "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/1c836a56-9162-42ff-b665-3502dc2856e0/posts",
#     json=sample_post,
# )
# print(resp.json())


url = "user/00000000-0000-0000-0000-000000000000/groups/047b32cd-0cae-4ba8-ac28-25eb0b538e3c/posts/90f751a9-1e7b-4b30-a02d-19d9b82111ae"

resp = requests.get(
    f"http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/c6a5cd0e-0f94-4a64-8e6f-74807d3efdad/posts/?s=0&limit=20"
)
print(resp.json())
