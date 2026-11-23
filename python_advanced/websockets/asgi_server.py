#!/usr/bin/env python3
"""ASGI application with an echo WebSocket endpoint."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Return the home page."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Echo every text message back to the sender."""
    await websocket.accept()
    try:
        while True:
            await websocket.send_text(await websocket.receive_text())
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
