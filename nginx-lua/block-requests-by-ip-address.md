# Block requests by IP address

```nginx
server {
  location / {
    content_by_lua_block {
      if ngx.var.remote_addr == "1.2.3.4" then
        ngx.say("no no no")
        ngx.exit(ngx.HTTP_FORBIDDEN)
      end
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.var.remote_addr` - returns client IP address
- `1.2.3.4` - sample IP address to block access for
- `ngx.say` - output given text to client
- `ngx.exit` - end response with specified status code
- `HTTP_FORBIDDEN` - 403 HTTP status code (see list of [all available codes](https://github.com/openresty/lua-nginx-module#http-status-constants))

group: ip


