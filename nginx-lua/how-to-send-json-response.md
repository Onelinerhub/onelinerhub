# How to send JSON response

```nginx
init_by_lua_block  {
  cjson = require("cjson")
}

server {
  location / {
    content_by_lua_block {
      local data = {name='Donald'}
      local output = cjson.encode(data)
      ngx.header["Content-type"] = 'application/json'
      ngx.say(output)
    }
  }
}
```

- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `require("cjson")` - load module to manipulate JSON
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `{name='Donald'}` - sample table to convert to JSON string
- `cjson.encode` - encodes given Lua table to JSON string
- `ngx.header` - allows to set response headers
- `application/json` - set content type to `application/json`
- `ngx.say` - output given text to client

## Example: 
```nginx
local data = {name='Donald'}
local output = cjson.encode(data)
ngx.header["Content-type"] = 'application/json'
ngx.say(output)
```
```
{"name":"Donald"}

```

