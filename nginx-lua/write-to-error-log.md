# Write to error log

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.log(ngx.ERR, "error text")
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.log` - logs given message
- `ngx.ERR` - we're going to write into error_log
- `"error text"` - message we want to log

group: log


