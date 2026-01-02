from starlette.applications import Starlette
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket
import asyncio
import time

async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    session_id = id(ws)

    try:
        await ws.send_text(f"connected: session={session_id}")

        while True:
            msg = await ws.receive_text()

            # Simulate processing latency
            await asyncio.sleep(0.2)

            await ws.send_text(f"echo [{time.time():.2f}]: {msg}")

    except Exception:
        pass
    finally:
        print(f"session closed: {session_id}")

routes = [
    WebSocketRoute("/ws", websocket_endpoint),
]

app = Starlette(routes=routes)
