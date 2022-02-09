# Get multiple keys values

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
local keys = redis:mget({'ma', 'mb'})
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `mget` - returns multiple keys values
- `{'ma', 'mb'}` - list of key names to get values for
- `keys` - will contain final values list

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:set('ma', '1')
redis:set('mb', '2')

local keys = redis:mget({'ma', 'mb'})
print( table.concat(keys, ', ') )
```
```
1, 2

```

