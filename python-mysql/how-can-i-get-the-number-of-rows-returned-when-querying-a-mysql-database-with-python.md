# How can I get the number of rows returned when querying a MySQL database with Python?
// plain

To get the number of rows returned when querying a MySQL database with Python, you can use the `cursor.rowcount` attribute of the `cursor` object. This attribute returns the number of rows that were affected by the last `SELECT` statement.

For example:
```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="passwd",
    database="mydatabase"
)

# Create a cursor object
my_cursor = mydb.cursor()

# Execute a query
my_cursor.execute("SELECT * FROM customers")

# Get the number of rows
num_rows = my_cursor.rowcount
print(num_rows)
```
## Output example

```
4
```

## Code explanation

1. Importing the `mysql.connector` library - `import mysql.connector`
2. Connecting to the database - `mydb = mysql.connector.connect(host="localhost", user="user", passwd="passwd", database="mydatabase")`
3. Creating a cursor object - `my_cursor = mydb.cursor()`
4. Executing a query - `my_cursor.execute("SELECT * FROM customers")`
5. Getting the number of rows - `num_rows = my_cursor.rowcount`
6. Printing the number of rows - `print(num_rows)`

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Cursor Object](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How can I get the number of rows returned when querying a MySQL database with Python?](https://onelinerhub.com/python-mysql/how-can-i-get-the-number-of-rows-returned-when-querying-a-mysql-database-with-python)