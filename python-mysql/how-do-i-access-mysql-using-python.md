# How do I access MySQL using Python?
// plain

To access MySQL using Python, you can use the `mysql.connector` library. This library allows you to connect to a MySQL database and perform various operations such as executing SQL statements, creating tables, and more.

Below is an example of how to connect to a MySQL database using Python:

```python
import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password"
)

# Print out the connection object
print(mydb)
```

The output of the above code will be a `MySQLConnection` object, which is used to perform operations on the MySQL database.

## Code explanation


- `import mysql.connector`: This imports the `mysql.connector` library, which allows you to connect to a MySQL database.

- `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password")`: This creates a connection to the MySQL database. The `host`, `user`, and `passwd` parameters are used to specify the hostname, username, and password, respectively.

- `print(mydb)`: This prints out the connection object, which is a `MySQLConnection` object.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [Python MySQL Tutorial](https://www.tutorialspoint.com/python3/python_database_access.htm)

onelinerhub: [How do I access MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-access-mysql-using-python)