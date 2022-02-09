# Redis eval example

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local val = redis:eval("return redis.call('get', 't1');", 0)
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `eval` - evaluates given LUA code directly on Redis server
- `return redis.call('get', 't1');` - Redis LUA code will return value for `t1` key

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('t1', '123')
local val = redis:eval("return redis.call('get', 't1');", 0)
print(val)
```
```
123

```

