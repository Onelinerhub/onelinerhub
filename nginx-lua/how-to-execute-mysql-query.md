# How to execute Mysql query

```nginx
init_by_lua_block {
  mysql = require "luasql.mysql"
}

server {
  location / {
    content_by_lua_block {
      local pool = mysql.mysql()
      local db = pool:connect('test', 'usr', 'pwd')
      
      local cursor = db:execute('SELECT * FROM table')
      row = cursor:fetch ({}, "a")
      while row do
        ngx.say(row.name)
        row = cursor:fetch ({}, "a")
      end
    }
  }
}
```

- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `mysql = require "luasql.mysql"` - load [Luarocks Mysql module](/nginx-lua/how-to-use-luarocks-modules-in-nginx-lua)
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `local pool = mysql.mysql()` - init connection pool
- `pool:connect('test', 'usr', 'pwd')` - connect to specified Mysql server
- `db:execute` - execute specified SQL
- `cursor:fetch` - return next row from Mysql results cursor
- `ngx.say` - output given text to client

## Example: 
```nginx
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT NOW() as n')
row = cursor:fetch ({}, "a")
ngx.say(row.n)
```
```
2022-03-23 16:40:28

```

