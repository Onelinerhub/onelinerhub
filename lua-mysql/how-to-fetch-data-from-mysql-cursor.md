# How to fetch data from Mysql cursor

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT id, name FROM test)
local row = cursor:fetch({})
while row do
  print(row[1], row[2])
  row = cursor:fetch({})
end

```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `db:execute` - executes given query and returns cursor to iterate through results
- `cursor:fetch({})` - fetch row from Mysql result set into numeric array
- `print(row[1], row[2])` - prints first and second column for each row

## Example: 
```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local cursor = db:execute('SELECT id, name FROM test LIMIT 5')
local row = cursor:fetch({})
while row do
  print(row[1], row[2])
  row = cursor:fetch({})
end

```
```
1	A
2	B
3	C
4	Donald
5	Donald

```

