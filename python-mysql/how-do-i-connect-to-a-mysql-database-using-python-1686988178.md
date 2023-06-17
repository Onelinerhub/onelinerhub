# How do I connect to a MySQL database using Python?
// plain

Connecting to a MySQL database with Python is a straightforward process. Here is an example of how to connect to a MySQL database using Python:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)

print(mydb)
```

## Output example


```
<mysql.connector.connection.MySQLConnection object at 0x7f3d7f2e9f50>
```

The code above consists of the following parts:

1. `import mysql.connector` - imports the MySQL Connector Python module.
2. `mydb = mysql.connector.connect(host="localhost", user="user", passwd="passwd")` - establishes a connection to the MySQL database server.
3. `print(mydb)` - prints the connection object to the console.

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I connect to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-a-mysql-database-using-python-1686988178)