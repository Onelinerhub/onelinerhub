# Making HTTP POST request

```lua
local http = require("socket.http")
local body, code, headers, status = http.request {
    method = "POST",
    url = "https://httpbin.org/post",
    source = 'var=1',
    headers = {
        ["content-type"] = "text/plain",
        ["content-length"] = '5'
    }
}

print(code)
```

- `require("socket.http")` - load standard HTTP utility lib
- `http.request` - sends GET request to the specified address
- `https://google.com` - sample URL
- `body, code, headers, status` - variables will store response body, code, headers and status

group: http

## Example: 
```lua
local http = require("socket.http")
local body, code, headers, status = http.request {
    method = "POST",
    url = "https://httpbin.org/post",
    
    headers = {
        ["content-type"] = "text/plain",
        ["content-length"] = '5'
    }
}

print(status)
```
```




lua: /usr/share/lua/5.3/ltn12.lua:290: attempt to call a string value (local 'src')
stack traceback:
	[C]: in function 'socket.http.request'
	/tmp/test.lua:2: in main chunk
	[C]: in ?
```

