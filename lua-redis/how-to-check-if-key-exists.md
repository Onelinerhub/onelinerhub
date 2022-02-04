# How to check if key exists

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local does_exist = redis:exists('key')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:exists` - will return `true` if specified key exists
- `'key'` - key name to check existence of
- `does_exist` - will contain `true` if specified key exists

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 'val')

local exists = redis:exists('key')
print(exists)

local exists = redis:exists('key1')
print(exists)
```
```
true
false

```

