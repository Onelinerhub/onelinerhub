# Upload file upload with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local upload = require "upload"

      local form, err = upload:new(4096)
      if not form then
        ngx.say(err)
        ngx.exit(200)
      end
      
      form:set_timeout(1000)
      file = io.open('/tmp/upload.tmp', "w+")
      
      while true do
        local typ, res, err = form:read()
        if not typ then
          ngx.say(err)
          return
        end
      
        if typ == "body" then
          file:write(res)
        end
      
        if typ == "eof" then
          break
        end
      end
      
      ngx.say("file uploaded")
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `require "upload"` - load [lib:lua-upload module](https://github.com/openresty/lua-resty-upload) to handle uploads, see how to [include modules](/nginx-lua/how-to-use-luarocks-modules-in-nginx-lua)
- `upload:new` - init upload `form` object to get uploaded data
- `if not form then` - handle upload errors
- `/tmp/upload.tmp` - we'll save uploaded data to this file on server
- `form:read()` - read next chunk of uploaded data
- `file:write(res)` - write chunk to the file on server
- `ngx.say("file uploaded")` - say something when upload is finished

## Example: 
```nginx
local upload = require "upload"

local form, err = upload:new(4096)
if not form then
  ngx.say(err)
  ngx.exit(200)
end

form:set_timeout(1000)
file = io.open('/tmp/upload.tmp', "w+")

while true do
  local typ, res, err = form:read()
  if not typ then
    ngx.say(err)
    return
  end

  if typ == "body" then
    file:write(res)
  end

  if typ == "eof" then
    break
  end
end

ngx.say("file uploaded")
```
```
no boundary defined in Content-Type

```

