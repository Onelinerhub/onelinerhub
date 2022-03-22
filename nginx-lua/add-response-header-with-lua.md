# Add response header with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header["X-Example"] = 'onelinerhub-example'
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers
- `X-Example` - sample header to set
- `onelinerhub-example` - sample value to set

group: set_header


