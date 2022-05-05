# Redis auth (user/password) usage

```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:auth('user:pwd')
```

- `require 'redis'` - load [lib:Redis](https://onelinerhub.com/lua-redis/how-to-install-lua-redis-module) module for Lua
- `connect` - connect to Redis server
- `'127.0.0.1', 6379` - Redis host and port to connect to
- `auth` - authenticate on Redis server
- `user:pwd` - username and password to auth on Redis server

## Example: 
```lua
local redis = (require 'redis').connect('127.0.0.1', 6379)
redis:auth('user:pwd')
```

link_youtube: https://youtu.be/xvUF3zNz74c
