# Prepend value to list using rpush

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:rpush('list_key', 'val')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `list_key` - key of the list
- `'val'` - value to prepend
- `rpush` - prepends specified value to the Redis list

group: list

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:rpush('list4', 'd')
redis:rpush('list4', 'c')
local list = redis:lrange('list4', 0, 1)
print(table.concat(list, ', '))
```
```
d, c

```

