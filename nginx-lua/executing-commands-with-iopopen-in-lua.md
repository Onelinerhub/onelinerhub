# Read shell command output with io.popen

```nginx
server {
  location / {
    content_by_lua_block {
      local handle = io.popen('date')
      local out = handle:read("*a")
      handle:close()
      ngx.say(out)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `io.popen` - execute specified shell command and return handle to read output
- `handle:read` - read data from handle (command output)
- `handle:close()` - close handle
- `ngx.say` - output given text to client

group: shell

## Example: 
```nginx
local handle = io.popen('date')
local out = handle:read("*a")
handle:close()
ngx.say(out)
```
```
Tue Mar 22 16:54:33 UTC 2022


```

