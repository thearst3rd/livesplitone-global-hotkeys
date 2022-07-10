# Global Hotkeys for LiveSplit One

This is a WIP script to enable global hotkeys with [LiveSplit One](https://one.livesplit.org).

## Requirements

```bash
pip install pynput websockets
```

## Usage

1. Ensure the requirements above are installed
2. For now, manually edit the `on_press` function in `lso-hotkeys.py` to use the hotkeys you would like. Current supported are "start/split", "reset", "skip", and "undo".
3. Run `python lso-hotkeys.py`
4. In LiveSplit One, click "Connect to Server" and enter `ws://localhost:5678`
5. Pressing hotkeys should now trigger events in LiveSplit One!
