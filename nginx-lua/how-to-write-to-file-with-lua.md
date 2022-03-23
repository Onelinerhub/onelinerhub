# with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      file = io.open('/tmp/hi.txt', 'w')
      file:write('hola')
      io.close(file)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `io.open` - opens specified file handler
- `/tmp/hi.txt` - path to file to write
- `'w'` - select this mode to be able to write to file
- `file:write` - writes specified string to file
- `io.close` - close file handler

group: files

## Example: 
```nginx
file = io.open('/tmp/hi.txt', 'w')
file:write('hola')
io.close(file)
```

