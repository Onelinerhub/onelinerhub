# How to delete keys by pattern

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local keys = redis:scan(0, {match='t_*', count=100})[2]

for i,k in ipairs(keys) do
  redis:del(k)
end
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `t_*` - pattern to delete keys on
- `for i,k in ipairs(keys) do` - iterate through found keys
- `del` - deletes specified key

group: delete

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)

redis:set('t_1', 1)
redis:set('t_2', 2)
redis:set('t_3', 3)
local keys = redis:scan(0, {match='t_*', count=100})[2]

for i,k in ipairs(keys) do
  redis:del(k)
end

print(redis:get('t_1'))
print(redis:get('t_2'))
print(redis:get('t_3'))
```
```
nil
nil
nil

```

