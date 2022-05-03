# How to read file

```lua
file = io.open('/var/www/examples/test.txt', 'r')
local data = file:read()
io.close(file)
```

- `io.open` - opens file handler
- `/var/www/examples/test.txt` - path to the file to open
- `'r'` - open file in reading mode
- `file:read()` - reads opened file content
- `data` - variable will contain file content
- `io.close` - closes file handler

group: files

## Example: 
```lua
file = io.open('/var/www/examples/test.txt', 'r')
local data = file:read()
io.close(file)
print(data)
```
```
hi!

```

link_youtube: https://youtu.be/2msu5kc2jvo
