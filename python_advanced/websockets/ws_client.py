#!/usr/bin/env python3
"""WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send text once and return the response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    """Print the response of the echo server."""
    uri = "ws://localhost:8765"
    response = await connect_and_send(uri, "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
