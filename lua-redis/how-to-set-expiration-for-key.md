# How to set expiration for key

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 'test')
redis:expire('key', 30)
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:set` - sets specified key value
- `:expire` - set expiration (in seconds) for the specified key
- `'key'` - key name to set expiration for
- `30` - our key will expire in 30 seconds

group: expire

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('key', 'test')
redis:expire('key', 30)
print(redis:ttl('key'))
```
```
60

```

