from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from src.middleware import group_usecase
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlmodel import select
from src.domain.model.group_model import GroupModel, StatusGroupScrape
router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str,WebSocket] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        self.disconnect(client_id)
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            self.active_connections.pop(client_id)

    async def send_personal_message(self, data: dict, client_id: str):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_json(data=data)

manager = ConnectionManager()


async def handle_message(message: str):
    pass

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(client_id,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            
            # data = {
            #     "type": "message",
            #     "data": data
            # }
            # await manager.send_personal_message(data=data, client_id)
            # await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(client_id)

        # await manager.broadcast(f"Client #{client_id} left the chat")
        

from fastapi.encoders import jsonable_encoder

class WebhookData(BaseModel):
    type: str
    data: dict
    message: str

@router.post("/webhook/{client_id}")
async def webhook(client_id: str, data: WebhookData ):
    if data.type == "next_post":
        query = select(GroupModel).where(GroupModel.hc_id == data.data["hc_id"], GroupModel.status != StatusGroupScrape.COMPLETED.value, GroupModel.user_id == client_id)
        items = await group_usecase.query_groups(query)
        
        if items and len(items) > 0:
            item = items[0]
            item.status = StatusGroupScrape.PROCESSING
            await group_usecase.update_group(item)
            
            await manager.send_personal_message({
                "process": "start",
                "type" : "post",
                "data": jsonable_encoder(item.model_dump()),
                "message" : "Start process scrape post in  group" + item.name
                }, client_id)
            

    # await manager.send_personal_message(data.model_dump(), client_id)
    # return {"status": "ok"}
    

@router.get("/health-check")
async def health_check():
    return {"status": "ok"}
