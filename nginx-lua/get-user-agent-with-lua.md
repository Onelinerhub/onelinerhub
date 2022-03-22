# Get user agent with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say( ngx.var.http_user_agent);
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.var` - access request query string parameters
- `ngx.say` - output given text to client
- `http_user_agent` - returns user agent value

group: variables

## Example: 
```nginx
ngx.say( ngx.var.http_user_agent);
```
```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36
```

