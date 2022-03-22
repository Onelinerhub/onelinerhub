# Get request headers with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say(ngx.req.raw_header())
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `ngx.req.raw_header()` - returns raw HTTP request headers ([online example](http://lua.onelinerhub.com/headers))

group: get_header


