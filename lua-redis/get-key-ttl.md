# Get key TTL

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local expires_in = redis:ttl('key')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `:ttl` - returns seconds it'll take specified key to expire (or `-1` if it's not expirable)
- `'key'` - name of the key to get expiration second for

group: expire

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:expire('key', 60)
print(redis:ttl('key'))
```
```
60

```

