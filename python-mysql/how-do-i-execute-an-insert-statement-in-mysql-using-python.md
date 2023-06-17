# How do I execute an INSERT statement in MySQL using Python?
// plain

To execute an INSERT statement in MySQL using Python, you must first import the MySQL Connector/Python module. This module provides an API for connecting to and working with MySQL databases.

Once the module is imported, you can establish a connection to the MySQL server. This can be done by creating a connection object using the `connect()` method, and passing in the necessary parameters (host, database, user, and password).

After establishing a connection to the MySQL server, you can then create a cursor object. The cursor object is used to execute SQL statements on the database.

To execute an INSERT statement, you can use the `execute()` method of the cursor object. This method takes the SQL statement as a parameter, and executes it on the database.

For example:
```
import mysql.connector

# Establish connection to MySQL server
conn = mysql.connector.connect(host="localhost", database="mydb", user="myuser", password="mypass")

# Create cursor object
cursor = conn.cursor()

# Execute INSERT statement
cursor.execute("INSERT INTO users (name, age) VALUES ('John', 25)")

# Commit changes to database
conn.commit()
```

This code will execute the INSERT statement on the database, which will add a new row to the `users` table with the values `John` and `25`.

## Code explanation

- `import mysql.connector`: imports the MySQL Connector/Python module
- `conn = mysql.connector.connect(host="localhost", database="mydb", user="myuser", password="mypass")`: establishes a connection to the MySQL server
- `cursor = conn.cursor()`: creates a cursor object
- `cursor.execute("INSERT INTO users (name, age) VALUES ('John', 25)")`: executes an INSERT statement on the database
- `conn.commit()`: commits changes to the database

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Cursor Objects](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How do I execute an INSERT statement in MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-execute-an-insert-statement-in-mysql-using-python)