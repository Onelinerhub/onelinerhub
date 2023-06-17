# How can I keep my MySQL connection alive when using Python?
// plain

The MySQL connection can be kept alive when using Python by setting the connection timeout of the connection object. This can be done by setting the `connect_timeout` parameter to a non-zero value.

For example,
```
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="passwd",
    connect_timeout=60
)

print(db)
```
## Output example

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f1b8e1b2fd0>
```

The above code will create a connection object `db` and set the connection timeout to 60 seconds. This ensures that the connection will stay alive for 60 seconds even if there is no activity on the connection.

## Code explanation

1. `import mysql.connector`: This imports the mysql.connector module.
2. `db = mysql.connector.connect(host="localhost", user="user", passwd="passwd", connect_timeout=60)`: This creates a connection object `db` and sets the connection timeout to 60 seconds.
3. `print(db)`: This prints the connection object `db`.

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Connection Arguments](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)

onelinerhub: [How can I keep my MySQL connection alive when using Python?](https://onelinerhub.com/python-mysql/how-can-i-keep-my-mysql-connection-alive-when-using-python)