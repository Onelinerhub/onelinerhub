# How to connect to Mysql

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')
```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `test` - name of the database to connect to
- `'usr', 'pwd'` - username and password to use for Mysql connection

## Example: 
```lua
--mysql = require "luasql.mysql"
--local pool = mysql.mysql()
--local db = pool:connect('test', 'usr', 'pwd')

--local cursor = db:execute('SELECT NOW()')

print(cursor)
```

