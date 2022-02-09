# Get hash value using hget

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:hget('hash_test', 'a')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `hash_test` - hash name
- `'a'` - key name
- `hget` - returns specified key value for a given hash

group: hash

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
print(redis:hget('htst', 'a'))
```
```
1

```

