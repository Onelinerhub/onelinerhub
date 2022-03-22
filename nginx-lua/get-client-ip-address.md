# Get client IP address

### See working example that [returns your IP address](http://lua.onelinerhub.com/ip) based on this code:

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say(ngx.var.remote_addr)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.var.remote_addr` - returns client IP address
- `ngx.say` - output given text to client

group: ip


