# Set key value

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 'val')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:set` - sets specified key value
- `key` - key name
- `'val'` - value to set

group: getset

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 'val')
print(redis:get('key'))
```
```
val

```

