# Implement whitelist access (access for specific IPs only)

```nginx
server {
  location / {
    content_by_lua_block {
      if not ngx.var.remote_addr ~= "1.2.3.4" then
        ngx.say("no no no")
        ngx.exit(ngx.HTTP_FORBIDDEN)
      end
      
      ngx.say('access allowed')
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.var.remote_addr` - returns client IP address
- `1.2.3.4` - sample IP address to allow access for (whitelist)
- `ngx.HTTP_FORBIDDEN` - HTTP code 403, see [list of available codes](https://github.com/openresty/lua-nginx-module#http-status-constants)
- `'access allowed'` - this will be sent to client if IP is allowed

group: ip

## Example: 
```nginx
if not ngx.var.remote_addr ~= "1.2.3.4" then
  ngx.say("no no no")
  ngx.exit(ngx.HTTP_FORBIDDEN)
end

ngx.say('access allowed')
```
```
no no no

```

