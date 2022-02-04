# Mysql and Lua usage example

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT * FROM test')
row = cursor:fetch ({}, "a")
while row do
  print(row.id)
  row = cursor:fetch ({}, "a")
end

```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `test` - name of the database to connect to
- `'usr', 'pwd'` - username and password to use for Mysql connection
- `db:execute` - executes given query and returns cursor to iterate through results
- `cursor:fetch ({}, "a")` - fetch next row from result set
- `while row do` - loop through all rows
- `print(row.id)` - sample code to process `row` table

## Example: 
```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT * FROM test LIMIT 5')
row = cursor:fetch ({}, "a")
while row do
  print(row.id, row.name)
  row = cursor:fetch ({}, "a")
end

```
```
1	A
2	B
3	C
4	Donald
5	Donald

```

