# How to update data

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

db:execute('UPDATE test SET name = "Bill" WHERE id = 14')
```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `db:execute` - executes given query and returns cursor to iterate through results
- `'UPDATE test SET name = "Bill" WHERE id = 14'` - sample `UPDATE` query


link_youtube: https://youtu.be/Ly80EDfYxxc
