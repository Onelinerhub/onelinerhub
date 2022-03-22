# How to get request body

```nginx
server {
  location / {
    content_by_lua_block {
      local request_body = ngx.req.get_body_data()  
      ngx.say(request_body)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.req.get_body_data()` - returns full request body (posted data)
- `request_body` - will contain request body
- `ngx.say` - output given text to client

## Example: 
```nginx
local request_body = ngx.req.get_body_data()  
ngx.say(request_body)
-- curl "http://lua.onelinerhub.com/test" --data "hola"
```
```
hola
```

