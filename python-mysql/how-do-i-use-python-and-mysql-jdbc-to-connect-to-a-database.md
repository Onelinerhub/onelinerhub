# How do I use Python and MySQL JDBC to connect to a database?
// plain

To use Python and MySQL JDBC to connect to a database, you need to first install the MySQL Connector/J JDBC driver. Once the driver is installed, you can create a connection to the database using the `connect()` method of the `mysql.connector.connect` class. The following example code shows how to do this:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```

## Output example

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f9f7f3b9f60>
```

The code above consists of the following parts:
1. `import mysql.connector` imports the `mysql.connector` module, which contains the necessary classes and functions for connecting to a MySQL database.
2. `mydb = mysql.connector.connect(...)` creates a `mysql.connector.connection_cext.CMySQLConnection` object, which is used to make a connection to the database.
3. `host="localhost"` specifies the hostname of the database server.
4. `user="yourusername"` specifies the username used to authenticate the connection.
5. `passwd="yourpassword"` specifies the password used to authenticate the connection.
6. `print(mydb)` prints out the `CMySQLConnection` object, which is the result of the `connect()` method.

Once the connection is established, you can use the `execute()` method of the `CMySQLConnection` object to execute SQL queries.

## Helpful links
- [MySQL Connector/J Documentation](https://dev.mysql.com/doc/connector-j/8.0/en/)
- [MySQL Connector/J Tutorial](https://dev.mysql.com/doc/connector-j/8.0/en/connector-j-usagenotes-connect-drivermanager.html)

onelinerhub: [How do I use Python and MySQL JDBC to connect to a database?](https://onelinerhub.com/python-mysql/how-do-i-use-python-and-mysql-jdbc-to-connect-to-a-database)