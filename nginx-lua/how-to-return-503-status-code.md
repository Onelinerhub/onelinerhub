# How to return 503 status code

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say('error happened')
      ngx.exit(ngx.HTTP_SERVICE_UNAVAILABLE)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `ngx.exit` - end response with specified status code
- `ngx.HTTP_SERVICE_UNAVAILABLE` - HTTP code 503, see [list of available codes](https://github.com/openresty/lua-nginx-module#http-status-constants)

group: status_code


