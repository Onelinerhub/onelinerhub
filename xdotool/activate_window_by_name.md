# How to activate a window by name from CLI

```bash
xdotool search --name " - Google Chrome" windowactivate %1
```

- xdotool - tool to manipulate mouse/keyboard from CLI (```apt install xdotool```)
- search - search for a window by name
- Google Chrome - we're activating Chrome browser window
- windowactivate - set found window to active

group: windows
