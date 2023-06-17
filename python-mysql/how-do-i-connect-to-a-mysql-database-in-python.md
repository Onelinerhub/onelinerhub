# How do I connect to a MySQL database in Python?
// plain

Connecting to a MySQL database in Python is relatively easy with the help of the mysql-connector-python library. To connect to a MySQL database, you will need to have the following information:
* Hostname: The hostname of the server hosting the database.
* Username: The username of the user who has access to the database.
* Password: The password of the user who has access to the database.
* Database: The name of the database you want to connect to.

Below is an example of how to connect to a MySQL database with the mysql-connector-python library:

```
import mysql.connector

# Establish connection with the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="mydatabase"
)

# Print out the connection object
print(mydb)

# Output: <mysql.connector.connection.MySQLConnection object at 0x7f9c220b7550>
```

In the example above, the `host` parameter is set to `localhost` which means that the MySQL database is running on the same machine. The `user` and `passwd` parameters are set to `username` and `password` respectively and the `database` parameter is set to `mydatabase`.

Once the connection is established, the connection object is printed out.

## Helpful links
* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
* [Connecting to MySQL Using Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)

onelinerhub: [How do I connect to a MySQL database in Python?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-a-mysql-database-in-python)