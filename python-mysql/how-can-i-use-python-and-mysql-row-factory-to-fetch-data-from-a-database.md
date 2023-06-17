# How can I use Python and MySQL row_factory to fetch data from a database?
// plain

Using Python and MySQL row_factory is a great way to fetch data from a database. Here is an example of how to do this:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydatabase"
)

# Create a cursor
mycursor = mydb.cursor()

# Set the row_factory to a dictionary
mycursor.row_factory = mysql.connector.DictCursor

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Fetch the results
result = mycursor.fetchall()

# Print the results
print(result)
```

## Output example

```
[{'id': 1, 'name': 'John', 'address': 'Highway 37'}, {'id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}, {'id': 3, 'name': 'Amy', 'address': 'Apple st 652'}]
```

The code above does the following:

1. Imports the `mysql.connector` module
2. Connects to the database
3. Creates a cursor
4. Sets the row_factory to a dictionary
5. Executes a query
6. Fetches the results
7. Prints the results

For more information on using Python and MySQL row_factory, see the following links:

- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)
- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)

onelinerhub: [How can I use Python and MySQL row_factory to fetch data from a database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-and-mysql-row-factory-to-fetch-data-from-a-database)