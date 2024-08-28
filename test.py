import requests
import json

# data = [
#     {
#         "link": "https://www.facebook.com/groups/113194777190399/",
#         "name": "🏘🏠 Cho Thuê Phòng Trọ - Nhà Nguyên Căn - Chung Cư - Ở Ghép Tại TP.HCM",
#         "privacy": "Công khai",
#         "members": " 392K thành viên ",
#         "post_per_day": " 10+ bài viết mỗi ngày",
#     }
# ]

# class InputPost(BaseModel):
#     title: str | None = None
#     images: str | None = None
#     video: str | None = None
#     link: str | None = None
#     post_date: str | None = None
#     owner_name: str | None = None
#     reaction: str | None = None
#     profile_owner_post: str | None = None
data = [
    {
        "title": "Thue phong tro quan 10",
        "images": None,
        "video": None,
        "link": "https://www.facebook.com/groups/113194777190399/",
        "post_date": "2024-09-01",
        "owner_name": "ThanhLoi",
        "reaction": "100",
        "profile_owner_post": "https://www.facebook.com/thanhloi",
    }
]


# resp = requests.post(
#     "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/6078d19c-e24f-4fff-886b-a90db94263d4/posts",
#     json={"data": data},
# )
# print(resp.json())
# resp = requests.post(
#     "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups",
#     json={"data": data},
# )
# print(resp.json())


# resp = requests.get(
#     "http://localhost:8001/user/6078d19c-e24f-4fff-886b-a90db94263d4/groups/?s=15&limit=15"
# )
# print(resp.json())

resp = requests.get(
    "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/6078d19c-e24f-4fff-886b-a90db94263d4/posts/?s=0&limit=15"
)
print(resp.json())
