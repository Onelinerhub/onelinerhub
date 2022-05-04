# Find keys using scan

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local keys = redis:scan(0, {match='t_*', count=100})[2]
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `redis:scan` - scans all keys based on specified rules
- `match` - match pattern for keys to search
- `count` - total amount of keys to check (to limit amount of work to be done)

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)

redis:set('t_1', 1);
redis:set('t_2', 2);
redis:set('t_3', 3);
local keys = redis:scan(0, {match='t_*', count=100})[2]

print(table.concat(keys, ', '))
```
```
t_1, t_2, t_3

```

link_youtube: https://youtu.be/sscl5VJFSag
