# How can I use Python to connect to a MySQL database using Latin1 encoding?
// plain

To connect to a MySQL database using Latin1 encoding in Python, you can use the [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) library. The following example code will connect to a database using Latin1 encoding.

```
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    charset='latin1'
)

print(mydb)
```

## Output example

```
<mysql.connector.connection.MySQLConnection object at 0x7f3c8f7f2b00>
```

The code above is composed of the following parts:

1. `import mysql.connector` imports the MySQL Connector/Python library.
2. `mydb = mysql.connector.connect(...)` creates a connection to the database with the given parameters.
3. `host="localhost"` specifies the hostname of the database server.
4. `user="yourusername"` specifies the username to use when connecting to the database.
5. `passwd="yourpassword"` specifies the password to use when connecting to the database.
6. `charset='latin1'` specifies the character set to use when connecting to the database.
7. `print(mydb)` prints the connection object.

onelinerhub: [How can I use Python to connect to a MySQL database using Latin1 encoding?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-connect-to-a-mysql-database-using-latin--encoding)