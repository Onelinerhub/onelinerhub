# How to use regex

```nginx
server {
  location / {
    content_by_lua_block {
      local str = 'Hi, Donald! Do you like Joe?';
      local n1, n2 = str:match('(D.+\\?)!.+(J.+)?')
      
      ngx.say(n1)
      ngx.say(n2)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `local str` - sample string to run regex on
- `n1, n2` - these variables will store captured groups from matches
- `str:match` - run regex expression on `str`
- `ngx.say` - output given text to client

## Example: 
```nginx
local str = 'Hi, Donald! Do you like Joe?';
local n1, n2 = str:match('(D.+\\?)!.+(J.+)?')

ngx.say(n1)
ngx.say(n2)
```
```
Donald
Joe

```

