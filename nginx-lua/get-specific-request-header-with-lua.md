# Get request header with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say(ngx.req.get_headers()['Accept'])
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `ngx.req.get_headers()` - returns table with request headers ([online example](http://lua.onelinerhub.com/get_header))
- `'Accept'` - sample header to get value of

group: get_header


