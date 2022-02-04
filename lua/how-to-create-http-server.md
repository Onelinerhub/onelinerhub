# How to create HTTP server

```lua
local server = require 'http.server'
local headers = require 'http.headers'

local srv = server.listen {
  host = 'localhost',
  port = 82,
  onstream = function (sv, out)
    local hdrs = out:get_headers()
    local method = hdrs:get(':method')
    local path = hdrs:get(':path') or '/'

    local rh = headers.new()
    rh:append(':status','200')
    rh:append('content-type','text/plain')

    out:write_headers(rh, false)
    out:write_chunk(("Received '%s' request on '%s' at %s\n"):format(method, path, os.date()), true)
  end
}

srv:listen()
srv:loop()
```

- `require 'http.` - loads [lib:lua-http](https://onelinerhub.com/lua/install-http-module-with-luarocks) module
- `server.listen` - launch HTTP server to listen for requests
- `localhost` - host to listen on
- `82` - port to listen on
- `onstream` - callback to process request and return response
- `method` - request method
- `path` - request path
- `out:write_headers` - send headers to response
- `out:write_chunk` - send text to response
- `srv:listen()` - launch our HTTP server

## Example: 
```lua
lua srv.lua
curl http://127.0.0.1:82/test
// ctrl+c to stop server
```
```
Received 'GET' request on '/test' at Fri Feb  4 13:42:53 2022

```

