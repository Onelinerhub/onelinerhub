# How to modify response header with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header["Content-type"] = 'text/json'
      ngx.say("[1,2,3]")
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers

group: set_header


