# How to insert data

```lua
mysql = require "luasql.mysql"
local pool = mysql.mysql()
local db = pool:connect('test', 'usr', 'pwd')

db:execute('INSERT INTO test SET name = "Donald"')
```

- `require "luasql.mysql"` - includes [lib:mysql](https://onelinerhub.com/lua-mysql/how-to-install-mysql-lib) module to work with database
- `mysql.mysql()` - init Mysql connection
- `pool:connect` - connect to Mysql server based on specified credentials
- `db:execute` - executes given query
- `INSERT INTO test SET name = "Donald"` - sample `INSERT` query to execute

group: insert


link_youtube: https://youtu.be/aoqc73ETSQs
