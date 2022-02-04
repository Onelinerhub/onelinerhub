# How to escape values for SQL query

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local sql = string.format("SELECT * FROM test WHERE name = '%s'", db:escape("Don'T"))
db:execute(sql)

print(sql)
```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `db:execute` - executes given query
- `string.format` - we're using `format` method to generate final SQL with escaped value
- `'%s'` - placeholder for value to insert here
- `db:escape` - escapes specified value (using native Mysql method)
- `("Don'T")` - value (unsafe in our case) to escape

## Example: 
```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

local sql = string.format("SELECT * FROM test WHERE name = '%s'", db:escape("Don'T"))
db:execute(sql)

print(sql)
```
```
SELECT * FROM test WHERE name = 'Don\'T'

```

