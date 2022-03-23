# How to return 200 status code

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say('not found')
      ngx.exit(ngx.HTTP_NOT_FOUND)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `ngx.exit` - end response with specified status code
- `ngx.HTTP_NOT_FOUND` - HTTP code 404, see [list of available codes](https://github.com/openresty/lua-nginx-module#http-status-constants)

group: status_code

## Example: 
```nginx
ngx.say('ho ho ho')
ngx.exit(ngx.HTTP_OK)
```
```
ho ho ho

```

