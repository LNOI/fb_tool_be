import requests
import json
from datetime import datetime

sample_group = {
    "link": "https://www.facebook.com/groups/113194777190399/",
    "name": "🏘🏠 Cho Thuê Phòng Trọ - Nhà Nguyên Căn - Chung Cư - Ở Ghép Tại TP.HCM",
    "privacy": "Công khai",
    "members": " 392K thành viên ",
    "post_per_day": " 10+ bài viết mỗi ngày",
}

# sample_post = {
#     "title": "Thue phong tro quan 10",
#     "images": None,
#     "video": None,
#     "link": "https://www.facebook.com/groups/113194777190399/",
#     "post_date": "2024-09-01",
#     "owner_name": "ThanhLoi",
#     "reaction": "100",
#     "profile_owner_post": "https://www.facebook.com/thanhloi",
# }
# groups = []

# for i in range(100):
#     sample_group["name"] = (
#         f"🏘🏠 Cho Thuê Phòng Trọ - Nhà Nguyên Căn - Chung Cư - Ở Ghép Tại TP.HCM {i}"
#     )
#     groups.append(sample_group)


# resp = requests.get(
#     "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups?s=0&limit=100"
# )

# groups = resp.json()

# for g in range(len(groups)):
#     print(groups[g]["id"])
#     posts = []
#     for i in range(100):
#         sample_post["name"] = (
#             f"🏘🏠 Cho Thuê Phòng Trọ - Nhà Nguyên Căn - Chung Cư - Ở Ghép Tại TP.HCM {g}"
#         )
#         sample_post["link"] = (
#             "https://www.facebook.com/groups/113194777190399/" + str(g) + str(i)
#         )
#         posts.append(sample_post)
#     resp = requests.post(
#         f"http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/{groups[g]['id']}/posts",
#         json={"data": posts},
#     )
#     print(resp.json())


# resp = requests.get(
#     "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/9eef3ea3-29b0-49ac-aa48-a742b4970154/posts?s=0&limit=15"
# )
# print(resp.json())

import random

random_comment = ["Tôi cần mua", "Tối cần thuê", "Tôi cần bán", "Tôi cần tìm"]

resp = requests.get(
    "http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups?s=0&limit=100"
)
groups = resp.json()

user_random = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8"]


comment_sample = {}
for group in groups:
    resp = requests.get(
        f"http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/{group['id']}/posts?s=0&limit=50"
    )
    posts = resp.json()

    for p in posts:
        comments = []
        for i in range(50):
            cm = {
                "content": random.choice(random_comment),
                "sender_name": random.choice(user_random),
                "sender_link": "https://www.facebook.com/thanhloi",
                "comment_date": datetime.now().isoformat(),
                "note": "note",
                "images": "https://www.facebook.com/thanhloi",
            }
            comments.append(cm)
        resp = requests.post(
            f"http://localhost:8001/user/00000000-0000-0000-0000-000000000000/groups/{group['id']}/posts/{p['id']}/comments",
            json={"data": comments},
        )
        print(resp.json())
