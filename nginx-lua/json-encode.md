# How to encode to JSON

```nginx
init_by_lua_block  {
  cjson = require("cjson")
}

server {
  location / {
    content_by_lua_block {
      local tbl = {name='Donald'}
      local json = cjson.encode(tbl)
      ngx.say(json)
    }
  }
}
```

- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `require("cjson")` - load module to manipulate JSON
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `{name='Donald'}` - sample table to convert to JSON string
- `cjson.encode` - encodes given Lua table to JSON string
- `ngx.say` - output given text to client

group: json

## Example: 
```nginx
ngx.say(cjson.encode({name='Donald'}))
```
```
{"name":"Donald"}

```

