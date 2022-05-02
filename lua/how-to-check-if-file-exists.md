# How to check if file exists

### We'll use `io.open` to try to open file and return `true` or `false` based on this attempt:

```lua
local file_exists = io.open('/tmp/test.txt', "r") ~= nil
```

- `file_exists` - will contain `true` if file exists, otherwise `false`
- `io.open` - opens file handler
- `/tmp/test.txt` - file to check existence of
- `~= nil` - compare value with `nil` (returned if there's no file)

group: files

## Example: 
```lua
local file_exists = io.open('/tmp/test.txt', "r") ~= nil
print(file_exists)

local file_exists = io.open('unknow.txt', "r") ~= nil
print(file_exists)
```
```
true
false

```

link_youtube: https://youtu.be/PY_9s_yBBxc
