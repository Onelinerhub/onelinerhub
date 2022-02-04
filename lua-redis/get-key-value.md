# Get key value

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:get('key')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:get` - gets value by key
- `;key'` - key name

group: getset

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
print(redis:get('key'))
```
```
val

```

