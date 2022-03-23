# How to generate UUID

```nginx
init_by_lua_block {
  local uuid = require("uuid")
}

server {
  location / {
    add_header Content-type text/plain;
    
    content_by_lua_block {
      ngx.say( uuid() )
    }
  }
}
```

- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `uuid()` - [lib:UUID module](https://luarocks.org/modules/tieske/uuid) function that returns generated UUID string value
- `require("uuid")` - load [Luarocks UUID module](/nginx-lua/how-to-use-luarocks-modules-in-nginx-lua)

## Example: 
```nginx
ngx.say( uuid() )
```
```
cbb297c0-14a9-46bc-ad91-1d0ef9b42df9
```

