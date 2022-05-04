# Get all hash values using hgetall

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local values = redis:hgetall('hash_test')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `hash_test` - hash name
- `hgetall` - returns all key/values from given hash

group: hash

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:hset('htst', 'a', '1')
redis:hset('htst', 'b', '2')
local values = redis:hgetall('htst')

for k,v in pairs(values) do
  print(k, v)
end
```
```
a	1
b	2

```

link_youtube: https://youtu.be/7VJIYrvFMrE
