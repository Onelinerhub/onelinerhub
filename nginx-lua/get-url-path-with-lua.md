# Get URL path with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say( ngx.var.request_uri );
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.var` - access request query string parameters
- `ngx.say` - output given text to client
- `request_uri` - will return request URL

group: variables

## Example: 
```nginx
ngx.say( ngx.var.request_uri );
```
```
/test

```

