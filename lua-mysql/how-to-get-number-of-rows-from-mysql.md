# How to get number of rows from Mysql

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT * FROM test')
local num = cursor:numrows()
```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `db:execute` - executes given query and returns cursor to iterate through results
- `cursor` - cursor to manipulate result set
- `:numrows()` - returns number of rows in a result set

## Example: 
```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT * FROM test')
local num = cursor:numrows()

print(num)
```
```
16

```

link_youtube: https://youtu.be/c8-GgRdk0kM
