# Get list values

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local list = redis:lrange('list_key', 0, 10)
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:lrange` - gets values of specified list
- `list_key` - key name of the Redis list to get
- `0, 10` - return list items starting from first (`0` index) and ending with `10th` item

group: list

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local list = redis:lrange('list4', 0, 1)
print(table.concat(list, ', '))
```
```
d, c

```

link_youtube: https://youtu.be/0vSBvwJ2bHY
