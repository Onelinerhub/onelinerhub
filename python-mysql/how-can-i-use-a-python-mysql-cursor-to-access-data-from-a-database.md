# How can I use a Python MySQL cursor to access data from a database?
// plain

The `cursor` object in Python is used to interact with databases. It allows you to execute SQL queries, fetch data from the result sets, call procedures, and more. To use a Python MySQL cursor to access data from a database, you need to first create a connection to the database. This can be done using the `connect()` method of the `MySQLConnection` class.

## Example code

```
from mysql.connector import MySQLConnection, Error

# Connect to the database
db_connection = MySQLConnection(user='root', password='password',
                               host='localhost', database='test')

# Create a cursor object
cursor = db_connection.cursor()
```

Once the connection is established, you can use the `execute()` method of the `cursor` object to execute any SQL query. For example, to select all records from a table named `users`, the following code can be used:

```
# Execute query
cursor.execute("SELECT * FROM users")

# Fetch all records
records = cursor.fetchall()

# Print records
print(records)
```

## Output example

```
[(1, 'John', 'Smith'), (2, 'Jane', 'Doe'), (3, 'Bob', 'Jones')]
```

The code above:

1. Establishes a connection to the database using the `MySQLConnection` class.
2. Creates a `cursor` object.
3. Executes a SQL query using the `execute()` method of the `cursor` object.
4. Fetches all records from the result set using the `fetchall()` method.
5. Prints the records.

## Helpful links

- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQLConnection Class](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection.html)
- [Cursor Class](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How can I use a Python MySQL cursor to access data from a database?](https://onelinerhub.com/python-mysql/how-can-i-use-a-python-mysql-cursor-to-access-data-from-a-database)