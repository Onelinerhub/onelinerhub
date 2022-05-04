# How to get last inserted ID

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

db:execute('INSERT INTO test SET name = "Joe"')
local id = db:getlastautoid()
```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `db:execute` - executes given query and returns cursor to iterate through results
- `:getlastautoid()` - returns last inserted ID for current connection
- `local id` - returned ID

group: insert

## Example: 
```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

db:execute('INSERT INTO test SET name = "Joe"')
local id = db:getlastautoid()

print(id)
```
```
19

```

link_youtube: https://youtu.be/XakvO2iH7jI
