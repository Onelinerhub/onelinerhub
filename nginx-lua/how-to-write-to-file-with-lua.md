# How to write to file with Lua

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


group: files

## Example: 
```nginx
file = io.open('/tmp/hi.txt', 'w')
file:write('hola')
io.close(file)
```

