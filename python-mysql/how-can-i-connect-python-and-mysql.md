# How can I connect Python and MySQL?
// plain

To connect Python and MySQL, you can use the `mysql.connector` module. This module provides an API which can be used to connect to a MySQL database.

## Example code

```
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydatabase"
)

# Print the connection object
print(conn)
```

## Output example

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f3c3f8f7e10>
```

The code above does the following:
1. Imports the `mysql.connector` module.
2. Connects to the database using the `connect` method. This requires passing in the host, user, password, and database name as parameters.
3. Prints out the connection object.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I connect Python and MySQL?](https://onelinerhub.com/python-mysql/how-can-i-connect-python-and-mysql)