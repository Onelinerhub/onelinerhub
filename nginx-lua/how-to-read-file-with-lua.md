# How to read file

```nginx
server {
  location / {
    content_by_lua_block {
      file = io.open('/tmp/hi.txt', 'r')
      local data = file:read()
      io.close(file)
      ngx.say(data)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `io.open` - opens specified file handler
- `/tmp/hi.txt` - path to file to read from
- `'r'` - use this mode to read file content
- `file:read` - reads file content
- `data` - this variable will store file content
- `ngx.say` - output given text to client

group: files

## Example: 
```nginx
file = io.open('/tmp/hi.txt', 'r')
local data = file:read()
io.close(file)
ngx.say(data)
```
```
hola

```

