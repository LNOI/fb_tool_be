from fastapi import APIRouter

router = APIRouter()

# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: dict[str,WebSocket] = {}
#
#     async def connect(self, client_id: str, websocket: WebSocket):
#         await websocket.accept()
#         self.disconnect(client_id)
#         self.active_connections[client_id] = websocket
#
#     def disconnect(self, client_id: str):
#         if client_id in self.active_connections:
#             self.active_connections.pop(client_id)
#
#     async def send_personal_message(self, data: dict, client_id: str):
#         if client_id in self.active_connections:
#             await self.active_connections[client_id].send_json(data=data)
#
# manager = ConnectionManager()
#
#
# async def handle_message(message: str):
#     pass
#
# @router.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: str):
#     await manager.connect(client_id,websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#
#     except WebSocketDisconnect:
#         manager.disconnect(client_id)


# class WebhookData(BaseModel):
#     type: str
#     data: dict
#     message: str

# import time

# @router.post("/webhook/{client_id}")
# async def webhook(client_id: UUID, data: WebhookData ):
#     print(data)
#     if data.type == "next_post":
#         hc_data = await hc_usecase.get_history(UUID(data.data["hc_id"]))
#         query = select(GroupModel).where(
#             GroupModel.hc_id == UUID(data.data["hc_id"]),
#             GroupModel.status == StatusGroupScrape.PENDING,
#             GroupModel.user_id == client_id
#         )
#         items = await group_usecase.query_groups(query)
#
#         if not items:
#             items = await group_usecase.query_groups(query)
#
#         if items and len(items) > 0:
#             item = items[0]
#             print(item)
#             item.status = StatusGroupScrape.PROCESSING
#             await group_usecase.update_group(item)
#
#             await manager.send_personal_message({
#                     "process": "start",
#                     "type" : "post",
#                     "data": jsonable_encoder(item.model_dump()),
#                     "message" : "Start process scrape post in  group" + item.name,
#                     "hc_id": data.data["hc_id"],
#                     "setting": {
#                         "number_of_group": hc_data.number_of_group,
#                         "number_of_post": hc_data.number_of_post,
#                         "number_of_comment": hc_data.number_of_comment,
#                     }
#                     }, str(client_id))
#


@router.get("/health-check")
async def health_check():
    return {"status": "ok"}
