# Using authentication with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local user = nil

      if ngx.var.http_authorization then
        local auth = ngx.decode_base64(string.sub(ngx.var.http_authorization, 7))
        
        _, _, login, pwd = string.find(auth, "(%w+):(%w+)")
        if (login == 'u') and (pwd == 'pwd') then
          user = login
          ngx.say('success loging in')
        end
      end
        
      if user == nil then
        ngx.header["WWW-Authenticate"] = 'Basic realm="Restricted"'
        ngx.exit(ngx.HTTP_UNAUTHORIZED)
      end
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.var.http_authorization` - this head is set when user enters login/password in browser
- `ngx.decode_base64` - decode given value from base64
- `login, pwd = string.find(auth, "(%w+):(%w+)")` - extract login and password from auth header
- `(login == 'u') and (pwd == 'pwd')` - check login (should be `u`) and password (should be `pwd`)
- `user = login` - set `user` variable if authed successfully
- `if user == nil then` - if not authed or wrong credentials
- `WWW-Authenticate` - send HTTP basic auth header to request login & password from user

## Example: 
```nginx
local user = nil

if ngx.var.http_authorization then
  local auth = ngx.decode_base64(string.sub(ngx.var.http_authorization, 7))
  
  _, _, login, pwd = string.find(auth, "(%w+):(%w+)")
  if (login == 'u') and (pwd == 'pwd') then
    user = login
    ngx.say('success loging in')
  end
end
  
if user == nil then
  ngx.header["WWW-Authenticate"] = 'Basic realm="Restricted"'
  ngx.exit(ngx.HTTP_UNAUTHORIZED)
end
```
```
false
```

