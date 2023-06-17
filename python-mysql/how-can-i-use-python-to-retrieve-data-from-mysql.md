# How can I use Python to retrieve data from MySQL?
// plain

You can use Python to retrieve data from MySQL by using the Python MySQL connector library. This library provides an interface for connecting to a MySQL database server and executing SQL statements.

## Example code

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Fetch all the results
myresult = mycursor.fetchall()

# Print the results
for x in myresult:
  print(x)
```

## Output example

```
(1, 'John', 'Lowstreet 4')
(2, 'Peter', 'Lowstreet 5')
(3, 'Amy', 'Lowstreet 6')
```

The code consists of the following parts:
1. Importing the MySQL Connector library - `import mysql.connector`
2. Connecting to the database - `mydb = mysql.connector.connect(host="localhost", user="user", passwd="passwd", database="mydatabase")`
3. Creating a cursor object - `mycursor = mydb.cursor()`
4. Executing a query - `mycursor.execute("SELECT * FROM customers")`
5. Fetching the results - `myresult = mycursor.fetchall()`
6. Printing the results - `for x in myresult: print(x)`

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I use Python to retrieve data from MySQL?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-retrieve-data-from-mysql)