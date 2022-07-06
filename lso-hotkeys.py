import asyncio
import websockets
import global_hotkeys

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def main():
    async with websockets.serve(register, "localhost", 5678):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
