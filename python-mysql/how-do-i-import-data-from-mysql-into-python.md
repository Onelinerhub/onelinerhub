# How do I import data from MySQL into Python?
// plain

To import data from MySQL into Python, you can use the `mysql.connector` library. This library allows you to connect to a MySQL database, and then query the database and return the results as a Python dictionary.

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

# Create a cursor (an instance)
cursor = db.cursor()

# Execute a query
query = "SELECT * FROM users"
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Print results
print(results)
```

Example output:
```
[(1, 'John', 'Doe'), (2, 'Jane', 'Doe')]
```

The code above can be broken down into the following parts:

1. Import the `mysql.connector` library
2. Connect to the database
3. Create a cursor
4. Execute a query
5. Fetch the results
6. Print the results

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I import data from MySQL into Python?](https://onelinerhub.com/python-mysql/how-do-i-import-data-from-mysql-into-python)