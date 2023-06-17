# How do I close a MySQL connection using Python?
// plain

To close a MySQL connection using Python, you must use the `close()` method of the MySQL connection object. This will close the connection to the MySQL server.

## Example code

```
# Import the mysql.connector library/module
import mysql.connector

# Establish a MySQL connection
myconn = mysql.connector.connect(host="localhost", user="user", passwd="passwd", database="mydatabase")

# Close the connection
myconn.close()
```

The code above will close the connection to the MySQL server.

## Code explanation

- `import mysql.connector`: This imports the mysql.connector library/module.
- `myconn = mysql.connector.connect(host="localhost", user="user", passwd="passwd", database="mydatabase")`: This establishes a MySQL connection.
- `myconn.close()`: This closes the connection to the MySQL server.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How do I close a MySQL connection using Python?](https://onelinerhub.com/python-mysql/how-do-i-close-a-mysql-connection-using-python)