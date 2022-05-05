# How to delete key

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:del(key)

```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `del` - deletes specified key
- `key` - key name to delete

group: delete

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)

redis:set('t_1', 1)
print(redis:get('t_1'))

redis:del('t_1')
print(redis:get('t_1'))
```
```
1
nil

```

link_youtube: https://youtu.be/eLbEoOP0Dc0
