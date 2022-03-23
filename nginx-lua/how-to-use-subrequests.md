# How to use subrequests

```nginx
server {
  location / {
    content_by_lua_block {
      local res = ngx.location.capture('/page?test=1')
      ngx.say(res.body)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.location.capture` - executes sync [Nginx subrequest](https://github.com/openresty/lua-nginx-module#ngxlocationcapture) to the specified URI
- `/page?test=1` - sample URL with arguments to make subrequest to
- `local res` - this table will have 4 fields: `status`, `header`, `body` and `truncated`

## Example: 
```nginx
local res = ngx.location.capture('/ip')
ngx.say(res.body)
```
```
3.123.32.182


```

