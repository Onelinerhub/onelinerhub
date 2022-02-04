# Append value to list using lpush

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:lpush('list_key', 'val')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `lpush` - appends value to the end of the Redis list
- `list_key` - key of the list
- `'val'` - value to append

group: list

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:lpush('list3', 'a')
redis:lpush('list3', 'b')
local list = redis:lrange('list3', 0, 1)
print(table.concat(list, ', '))
```
```
b, a

```

