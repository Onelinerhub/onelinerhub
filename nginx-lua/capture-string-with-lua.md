# Capture string with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local date = "24.02.2022"
      _, _, d, m, y = string.find(date, "(%d+).(%d+).(%d+)")
      ngx.say(m, '/', d, '/', y)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `date = "24.02.2022"` - sample string
- `string.find` - captures found substrings and returns to a given list of variables
- `"(%d+).(%d+).(%d+)"` - expression to capture by
- `ngx.say` - output given text to client

group: string

## Example: 
```nginx
local date = "24.02.2022"
_, _, d, m, y = string.find(date, "(%d+).(%d+).(%d+)")
ngx.say(m, '/', d, '/', y)
```
```
02/24/2022

```

