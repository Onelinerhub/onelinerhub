# Set hash value using hset

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:hset('hash_test', 'a', '1')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `hset` - sets key value of specified hash
- `hash_test` - hash name
- `'a'` - key name
- `'1'` - key value

group: hash

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)

redis:hset('htst', 'a', '1')
redis:hset('htst', 'b', '2')

print(redis:hget('htst', 'b'))
print(redis:hget('htst', 'a'))
```
```
2
1

```

link_youtube: https://youtu.be/z00ziolT1co
