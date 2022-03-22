# How to write JSON to log

```nginx
log_format log_json '$json';
init_by_lua 'cjson = require("cjson")';

server {
  location / {
    set_by_lua_block $json {
      return cjson.encode({http_version=ngx.req.http_version(), uri=ngx.var.request_uri})
    }
    
    access_log /var/log/nginx/json.log log_json;
  }
}
```

- `log_format` - specify custom log format to log request body
- `log_json` - log format name
- `$json` - this variable will contain JSON to log
- `init_by_lua` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `set_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive that sets specified variable with a result from Lua code
- `cjson.encode` - encodes given Lua table to JSON string
- `http_version=ngx.req.http_version()` - sample JSON key and value (just to show you can populate with anything)
- `access_log` - set access log path and format

group: log


