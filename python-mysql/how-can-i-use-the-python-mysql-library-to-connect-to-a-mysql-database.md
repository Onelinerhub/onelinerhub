# How can I use the Python MySQL library to connect to a MySQL database?
// plain

To use the Python MySQL library to connect to a MySQL database, you need to first install the library and then import it into your code.

## Example code

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
<mysql.connector.connection.MySQLConnection object at 0x7f5f6d4f7d90>
```

The code above will:

1. Import the MySQL library: `import mysql.connector`
2. Establish a connection to the database using the `mysql.connector.connect()` method, which takes in parameters such as the host, user, and password.
3. Print the connection object to the console.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I use the Python MySQL library to connect to a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-the-python-mysql-library-to-connect-to-a-mysql-database)