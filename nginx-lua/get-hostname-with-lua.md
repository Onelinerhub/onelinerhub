# Get hostname with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say( ngx.var.host );
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `ngx.var` - access Nginx variables
- `host` - variable with hostname value

group: variables

## Example: 
```nginx
ngx.say( ngx.var.host );
```
```
lua.onelinerhub.com

```

