# How do I enable autocommit in Python MySQL?
// plain

To enable autocommit in Python MySQL, you need to use the `autocommit` method of the `MySQLConnection` object. This method takes a boolean value, `True` to enable autocommit, or `False` to disable it.

## Example code

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mydb.autocommit = True
```

## Code explanation

1. `import mysql.connector` - imports the mysql.connector module
2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")` - connects to the MySQL database
3. `mycursor = mydb.cursor()` - creates a cursor object
4. `mydb.autocommit = True` - enables autocommit

## Helpful links
- [MySQL Documentation - autocommit](https://dev.mysql.com/doc/refman/8.0/en/commit.html)
- [MySQL Connector/Python Documentation - autocommit](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-autocommit.html)

onelinerhub: [How do I enable autocommit in Python MySQL?](https://onelinerhub.com/python-mysql/how-do-i-enable-autocommit-in-python-mysql)