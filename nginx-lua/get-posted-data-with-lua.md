# Get post variable value

```nginx
server {
  location / {
    content_by_lua_block {
      local test = ngx.req.get_post_args()["test"]
      ngx.say(test)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.req.get_post_args()` - get all posted variables
- `"test"` - sample post variable to get value of
- `ngx.say` - output given text to client

## Example: 
```nginx
local test = ngx.req.get_post_args()["test"]
ngx.say(test)
-- request "curl "localhost/test" --data "test=123""
```
```
123

```

