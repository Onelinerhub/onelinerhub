# How to modify response header with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header["Content-type"] = 'application/json'
      ngx.say("[1,2,3]")
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers
- `Content-type` - response header to modify
- `application/json` - new header value to set
- `ngx.say` - output given text to client
- `[1,2,3]` - sample text in JSON format to output ([online example](http://lua.onelinerhub.com/mod_header))

group: set_header


