# How to parse JSON

```nginx
init_by_lua_block  {
  cjson = require("cjson")
}

server {
  location / {
    content_by_lua_block {
      local json = '{"name":"Donald"}'
      local tbl = cjson.decode(json)
      ngx.say(tbl['name'])
    }
  }
}
```

- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `require("cjson")` - load module to manipulate JSON
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `'{"name":"Donald"}'` - sample JSON string to parse
- `cjson.decode` - parses given JSON string into table
- `tbl['name']` - get `name` key value from `tbl` table which has parsed data from JSON
- `ngx.say` - output given text to client

group: json

## Example: 
```nginx
local json = '{"name":"Donald"}'
local tbl = cjson.decode(json)
ngx.say(tbl['name'])
```
```
Donald

```

