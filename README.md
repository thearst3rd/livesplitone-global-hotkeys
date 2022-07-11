# Global Hotkeys for LiveSplit One

This is a WIP python script to enable global hotkeys with [LiveSplit One](https://one.livesplit.org). It uses [pynput](https://pypi.org/project/pynput/) which enables cross-platform reading of global keypresses.

## Requirements

* Python 3
	* [`pynput`](https://pypi.org/project/pynput/)
	* [`websockets`](https://pypi.org/project/websockets/)

If you have python installed, you can install the dependancies with following command:

```bash
pip install pynput websockets
```

## Usage

1. Ensure the requirements above are installed
2. For now, manually edit the `on_press` function in `ls1-hotkeys.py` to use the hotkeys you would like. Current supported are "start/split", "reset", "skip", and "undo".
3. Run `python ls1-hotkeys.py`
4. In LiveSplit One, click "Connect to Server" and enter `ws://localhost:5678`
5. Pressing hotkeys should now trigger events in LiveSplit One!
