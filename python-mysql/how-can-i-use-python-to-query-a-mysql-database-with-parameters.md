# How can I use Python to query a MySQL database with parameters?
// plain

To query a MySQL database with parameters using Python, you can use the `MySQL Connector/Python` library. This library provides an API for accessing and manipulating databases from Python.

Below is an example of how to use `MySQL Connector/Python` to query a MySQL database with parameters:

```
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define the query
sql = "SELECT * FROM customers WHERE address = %s"

# Define the parameters
params = ("Valley 345", )

# Execute the query
mycursor.execute(sql, params)

# Fetch the results
myresult = mycursor.fetchall()

# Print the results
print(myresult)
```

## Output example

```
[('Peter', 'Lowstreet 4', 'Valley 345'),
 ('Amy', 'Apple st 652', 'Valley 345')]
```

This code does the following:
1. Imports the `mysql.connector` library, which provides an API for accessing and manipulating databases from Python.
2. Connects to a MySQL database.
3. Creates a cursor object to execute the query.
4. Defines the query and the parameters.
5. Executes the query with the parameters.
6. Fetches the results.
7. Prints the results.

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [How can I use Python to query a MySQL database with parameters?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-query-a-mysql-database-with-parameters)