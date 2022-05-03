# Making HTTP GET request

```lua
local http = require("socket.http")
local ltn12 = require 'ltn12'

local body = {}
local res, code, headers, status = http.request{
  url = "https://httpbin.org/get",
  sink = ltn12.sink.table(body)
}

local response = table.concat(body)
```

- `require("socket.http")` - load standard HTTP utility lib
- `http.request` - sends GET request to the specified address
- `https://httpbin.org/get` - sample URL
- `res, code, headers, status` - variables will store response result, code, headers and status
- `response` - variable will store full content from HTTP response

group: http

## Example: 
```lua
local http = require("socket.http")
local ltn12 = require 'ltn12'

local body = {}
local res, code, headers, status = http.request{
  url = "https://httpbin.org/get",
  sink = ltn12.sink.table(body)
}

local response = table.concat(body)
print(response)
```
```
{
  "args": {}, 
  "headers": {
    "Host": "httpbin.org", 
    "User-Agent": "LuaSocket 3.0-rc1", 
    "X-Amzn-Trace-Id": "Root=1-61fd256f-747261a67fe983a70786f02e"
  }, 
  "origin": "3.123.32.182", 
  "url": "http://httpbin.org/get"
}


```

link_youtube: https://youtu.be/9YzvAODvsVI
