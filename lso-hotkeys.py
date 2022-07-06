import asyncio
import websockets
import threading
from pynput import keyboard


CONNECTIONS = set()


def on_press(key):
	print(type(key), key)
	if key == keyboard.KeyCode.from_char('0'):
		print("split")
		websockets.broadcast(CONNECTIONS, "split")
		websockets.broadcast(CONNECTIONS, "start")
	elif key == keyboard.KeyCode.from_char('3'):
		print("reset")
		websockets.broadcast(CONNECTIONS, "reset")
	elif key == keyboard.KeyCode.from_char('2'):
		print("skip")
		websockets.broadcast(CONNECTIONS, "skip")
	elif key == keyboard.KeyCode.from_char('8'):
		print("undo")
		websockets.broadcast(CONNECTIONS, "undo")


async def register(websocket):
	CONNECTIONS.add(websocket)
	print("websocket connected")
	try:
		await websocket.wait_closed()
		print("websocket closed")
	finally:
		CONNECTIONS.remove(websocket)


async def main():
	async with websockets.serve(register, "localhost", 5678):
		await asyncio.Future()


if __name__ == "__main__":
	# Make keyboard listener thread
	listener = keyboard.Listener(
		on_press=on_press)
	listener.start()

	asyncio.run(main())
