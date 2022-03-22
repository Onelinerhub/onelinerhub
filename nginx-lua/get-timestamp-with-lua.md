# Get timestamp with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local ts = os.time()
      ngx.say(ts)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `os.time()` - returns current unix timestamp in seconds
- `ngx.say` - output given text to client

group: time

## Example: 
```nginx
local ts = os.time()
ngx.say(ts)
```
```
1647970166

```

