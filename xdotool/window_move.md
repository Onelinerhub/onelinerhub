# How to move a window from CLI

```bash
xdotool getactivewindow windowmove 10 50
```

- xdotool - tool to manipulate mouse/keyboard from CLI (```apt install xdotool```)
- getactivewindow - will operate on currently [active window](/xdotool/activate_window_by_name)
- windowmove - move a window to specified X/Y coordinates
- 10 - X coordinate
- 50 - Y coordinate

group: windows
