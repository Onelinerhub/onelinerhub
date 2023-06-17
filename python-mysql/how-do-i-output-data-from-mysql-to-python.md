# How do I output data from MySQL to Python?
// plain

To output data from MySQL to Python, you can use the `mysql.connector` library. This library allows you to connect to a MySQL database and execute SQL queries from within Python.

For example, to select and print all rows from a table named `employees`:

```
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="passwd",
    database="mydatabase"
)

# Create a cursor (an object to iterate over the results)
cursor = db.cursor()

# Execute the query
cursor.execute("SELECT * FROM employees")

# Fetch and print the results
result = cursor.fetchall()
for x in result:
  print(x)
```

## Output example

```
(1, 'John', 'Doe', 'john@example.com')
(2, 'Mary', 'Moe', 'mary@example.com')
(3, 'Julie', 'Dooley', 'julie@example.com')
```

The code above consists of the following parts:

1. Importing the `mysql.connector` library
2. Connecting to the database
3. Creating a cursor
4. Executing the query
5. Fetching and printing the results

For more information, see the [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I output data from MySQL to Python?](https://onelinerhub.com/python-mysql/how-do-i-output-data-from-mysql-to-python)