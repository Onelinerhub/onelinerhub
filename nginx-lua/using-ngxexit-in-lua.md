# Using ngx.exit in Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say('ho ho ho')
      ngx.exit(ngx.HTTP_OK)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `ngx.exit` - end response with specified status code
- `ngx.HTTP_OK` - HTTP code 200, see [list of available codes](https://github.com/openresty/lua-nginx-module#http-status-constants)

## Example: 
```nginx
ngx.say('ho ho ho')
ngx.exit(ngx.HTTP_OK)
```
```
ho ho ho

```

