from fastapi import WebSocket, WebSocketDisconnect
from typing import List

active_connections: List[WebSocket] = []

async def handle_connection(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming messages
            await broadcast(f"Message received: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)

async def broadcast(message: str):
    for connection in active_connections:
        await connection.send_text(message)