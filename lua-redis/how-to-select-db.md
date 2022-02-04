# How to select db

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:select(2)
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:select` - selects specified DB by number
- `(2)` - select DB number `2`

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
print(redis:get('key'))

redis:select(2)
print(redis:get('key'))
```
```
10
nil

```

