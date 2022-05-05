# Lua and Redis usage example

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('k1', 'hi')
print(redis:get('k1'))
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:set` - set key value
- `'k1'` - key name
- `'hi'` - value to set
- `:get` - gets value by key

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('k1', 'hi')
print(redis:get('k1'))
```
```
hi

```

link_youtube: https://youtu.be/kuXNcq_N-pk
