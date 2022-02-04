# Making HTTP request

```lua
local http = require("socket.http")
local body, code, headers, status = http.request("https://google.com")
```

- `require("socket.http")` - load standard HTTP utility lib
- `http.request` - sends GET request to the specified address
- `https://google.com` - sample URL
- `body, code, headers, status` - variables will store response body, code, headers and status

group: http

## Example: 
```lua
local http = require("socket.http")
local body, code, headers, status = http.request("https://google.com")

print(status)
```
```
200
HTTP/1.1 200 OK

```

