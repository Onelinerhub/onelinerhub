# How can I use Python to make a MySQL request?
// plain

You can use Python to make a MySQL request using the MySQL Connector/Python library. The following example code connects to a MySQL database and makes a select query:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

# Create a cursor
my_cursor = mydb.cursor()

# Execute a query
my_cursor.execute("SELECT * FROM customers")

# Fetch all results
result = my_cursor.fetchall()

# Print the results
print(result)
```

## Output example

```
[(1, 'John', 'Highway 21'), (2, 'Peter', 'Lowstreet 4'), (3, 'Amy', 'Apple st 652'), (4, 'Hannah', 'Mountain 21'), (5, 'Michael', 'Valley 345')]
```

## Code explanation


1. `import mysql.connector` - this imports the MySQL Connector/Python library.
2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")` - this creates a connection to the MySQL database.
3. `my_cursor = mydb.cursor()` - this creates a cursor which allows us to execute queries.
4. `my_cursor.execute("SELECT * FROM customers")` - this executes a select query to retrieve all records from the customers table.
5. `result = my_cursor.fetchall()` - this fetches all the results from the query.
6. `print(result)` - this prints the results.

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I use Python to make a MySQL request?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-make-a-mysql-request)