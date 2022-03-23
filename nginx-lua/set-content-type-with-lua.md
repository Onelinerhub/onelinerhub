# How to set content type

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header["Content-type"] = 'text/html'
      ngx.say('<b>i am html</b>')
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers
- `Content-type` - response header to set
- `text/html` - set content type to `text/html`
- `ngx.say` - output given text to client


