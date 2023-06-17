# How can I set a timeout for a MySQL connection in Python?
// plain

To set a timeout for a MySQL connection in Python, you can use the `connect()` method from the `MySQLdb` module. This method takes an optional `connect_timeout` parameter which specifies the timeout in seconds.

For example:
```
import MySQLdb

db = MySQLdb.connect(host="localhost", user="user", passwd="password", connect_timeout=5)
```

This will set the connection timeout to 5 seconds.

The `connect()` method also takes other optional parameters such as `db`, `port`, `unix_socket`, `charset`, `sql_mode`, `read_default_file`, `conv`, `use_unicode`, `client_flag`, `cursorclass`, `init_command`, `ssl` and `read_default_group`.

For more information, see the following links:
- [MySQLdb.connect()](https://mysqlclient.readthedocs.io/user_guide.html#connecting-to-mysql)
- [MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)

onelinerhub: [How can I set a timeout for a MySQL connection in Python?](https://onelinerhub.com/python-mysql/how-can-i-set-a-timeout-for-a-mysql-connection-in-python)