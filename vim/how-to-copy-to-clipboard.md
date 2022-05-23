# How to copy text to clipboard

### You can either copy to OS clipboard selecting text with mouse and pressing `Shift+Ctrl+c` or internal VIM buffer. Press `Esc` to [switch to command mode](/vim/how-to-switch-to-command-mode) and then type (then press `Enter`):

```text
v
[select text]
y
```

- `v` - first press `v` to switch to visual mode and move cursor to select text to copy
- `y` - once ready press `y` to yank text

group: clipboard


