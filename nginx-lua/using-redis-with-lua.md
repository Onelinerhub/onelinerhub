# Using Redis with Lua

```nginx
server {
  location /redis {
    add_header Content-type text/plain;

    content_by_lua_block {
      local redis = require "nginx.redis"
      local red = redis:new()
      red:connect("127.0.0.1", 6379)

      if ngx.var.arg_get then
        ngx.say(red:get(ngx.var.arg_get))
      end

      if ngx.var.arg_set then
        red:set(ngx.var.arg_set, ngx.var.arg_val)
        ngx.say("saved value " .. ngx.var.arg_val)
      end
    }
  }
}
```

- `server {` - virtual host configuration block
- `location` - specific location (group of URLs) configuration
- `/redis {` - handle all `/redis...` requests
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `require "nginx.redis"` - load [lib:redis](/nginx-lua/using-redis-with-lua-copy) modle
- `red:connect` - connect to Redis server
- `red:get` - get Redis value by specified key, see [online demo](http://lua.onelinerhub.com/redis?get=test)
- `red:set` - save value to Redis by specified key

group: redis


