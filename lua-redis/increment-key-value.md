# Increment key value

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 11)
redis:incr('key')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:set` - sets specified key value
- `:incr` - increments specified key
- `'key'` - key name to increment

group: incr_decr

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 11)
redis:incr('key')
print( redis:get('key') )
```
```
12

```

