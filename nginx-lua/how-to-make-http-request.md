# How to make HTTP request

```nginx
server {
  location / {
    content_by_lua_block {
      local http = require("socket.http")
      local ltn12 = require 'ltn12'
      
      local body = {}
      local res, code, headers, status = http.request{
        url = "https://httpbin.org/get",
        sink = ltn12.sink.table(body)
      }
      
      local response = table.concat(body)
      ngx.say(response)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `require("socket.http")` - library to make HTTP requests
- `response` - will contain response after request is done
- `ngx.say` - output given text to client

## Example: 
```nginx
local http = require("socket.http")
local ltn12 = require 'ltn12'

local body = {}
local res, code, headers, status = http.request{
  url = "https://httpbin.org/get",
  sink = ltn12.sink.table(body)
}

local response = table.concat(body)
ngx.say(response)
```
```
{
  "args": {}, 
  "headers": {
    "Host": "httpbin.org", 
    "User-Agent": "LuaSocket 3.0-rc1", 
    "X-Amzn-Trace-Id": "Root=1-6239f151-16a98caa7dba3b427f959567"
  }, 
  "origin": "3.123.32.182", 
  "url": "http://httpbin.org/get"
}


```

## Additional keywords
- curl

