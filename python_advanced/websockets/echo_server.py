#!/usr/bin/env python3
"""Echo WebSocket server."""
import asyncio
import websockets


async def connection_handler(websocket):
    """Send back every message received."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the server."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
