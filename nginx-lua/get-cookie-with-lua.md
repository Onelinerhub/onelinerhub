# Get cookie with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local val = ngx.var.cookie_somecookie
      ngx.say(val)
    }
  }
}
```


group: cookie

## Example: 
```nginx
local val = ngx.var.cookie_somecookie
ngx.say(val)
```
```
123
```

