# Making HTTP POST request

```lua
local http = require("socket.http")
local ltn12 = require"ltn12"
local body = {}

local res, code, headers, status = http.request {
    method = "POST",
    url = "https://httpbin.org/post",
    source = ltn12.source.string('var=123'),
    headers = {
        ["content-type"] = "text/plain",
        ["content-length"] = '7'
    },
    sink = ltn12.sink.table(body)
}

response = table.concat(body)
```

- `require("socket.http")` - load standard HTTP utility lib
- `body = {}` - declare variable to save response body to
- `http.request` - sends specified HTTP request
- `res, code, headers, status` - variables will store response result, code, headers and status
- `"POST"` - send POST request
- `https://httpbin.org/post` - URL to post to
- `'var=123'` - data to post to
- `headers` - specify header to send
- `sink` - collect response body into specified `body` variable
- `response` - will contain full response text

group: http

## Example: 
```lua
local http = require("socket.http")
local ltn12 = require"ltn12"
local body = {}

local res, code, headers, status = http.request {
    method = "POST",
    url = "https://httpbin.org/post",
    source = ltn12.source.string('var=123'),
    headers = {
        ["content-type"] = "text/plain",
        ["content-length"] = '7'
    },
    sink = ltn12.sink.table(body)
}

print(table.concat(body))
```
```
{
  "args": {}, 
  "data": "var=123", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Content-Length": "7", 
    "Content-Type": "text/plain", 
    "Host": "httpbin.org", 
    "User-Agent": "LuaSocket 3.0-rc1", 
    "X-Amzn-Trace-Id": "Root=1-61fd22ff-798910395122567b557f334b"
  }, 
  "json": null, 
  "origin": "3.123.32.182", 
  "url": "http://httpbin.org/post"
}


```

