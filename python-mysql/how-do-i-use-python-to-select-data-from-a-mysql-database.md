# How do I use Python to select data from a MySQL database?
// plain

To use Python to select data from a MySQL database, you can use the `mysql.connector` module. This module provides an API for connecting to and interacting with a MySQL database.

## Example code


```
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydatabase"
)

# Create a cursor object
cursor = db.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch the results
result = cursor.fetchall()

# Print the results
print(result)
```

## Output example


```
[(1, 'John', 'Doe', 'john@example.com'), (2, 'Jane', 'Doe', 'jane@example.com')]
```

The code above can be broken down into the following parts:

1. Import the `mysql.connector` module.
2. Connect to the database using `mysql.connector.connect()` and passing in the relevant connection details.
3. Create a cursor object using `db.cursor()`.
4. Execute a query using `cursor.execute()`.
5. Fetch the results using `cursor.fetchall()`.
6. Print the results.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How do I use Python to select data from a MySQL database?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-select-data-from-a-mysql-database)