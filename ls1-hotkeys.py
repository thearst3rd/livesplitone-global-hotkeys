# Global Hotkeys for LiveSplit One
# by thearst3rd

import asyncio
import websockets
from pynput import keyboard


# Configure your preferred hotkeys here. For details, see:
# https://pynput.readthedocs.io/en/latest/keyboard.html
split_hotkey = keyboard.KeyCode.from_char('1')
reset_hotkey = keyboard.KeyCode.from_char('3')
undo_hotkey = keyboard.KeyCode.from_char('8')
skip_hotkey = keyboard.KeyCode.from_char('2')
pause_hotkey = keyboard.KeyCode.from_char('5')

debug_print_all_keys = False


CONNECTIONS = set()


def on_press(key):
	if debug_print_all_keys:
		print(type(key), key)

	if key == split_hotkey and split_hotkey is not None:
		print("splitOrStart")
		websockets.broadcast(CONNECTIONS, '{"command": "splitOrStart"}')
	elif key == reset_hotkey and reset_hotkey is not None:
		print("reset")
		websockets.broadcast(CONNECTIONS, '{"command": "reset"}')
	elif key == undo_hotkey and undo_hotkey is not None:
		print("undo")
		websockets.broadcast(CONNECTIONS, '{"command": "undoSplit"}')
	elif key == skip_hotkey and skip_hotkey is not None:
		print("skip")
		websockets.broadcast(CONNECTIONS, '{"command": "skipSplit"}')
	elif key == pause_hotkey and pause_hotkey is not None:
		print("togglePauseOrStart")
		websockets.broadcast(CONNECTIONS, '{"command": "togglePauseOrStart"}')


async def register(websocket):
	CONNECTIONS.add(websocket)
	print("websocket connected")
	try:
		await websocket.wait_closed()
		print("websocket closed")
	finally:
		CONNECTIONS.remove(websocket)


async def main():
	address = "localhost"
	port = 5678
	async with websockets.serve(register, address, port) as server:
		print(f"Global hotkeys running! Connect LiveSplit One to ws://{address}:{port}")
		await asyncio.Future()


if __name__ == "__main__":
	# Make keyboard listener thread
	listener = keyboard.Listener(
		on_press = on_press)
	listener.start()

	asyncio.run(main())
