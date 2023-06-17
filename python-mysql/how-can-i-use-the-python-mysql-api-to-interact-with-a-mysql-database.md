# How can I use the Python MySQL API to interact with a MySQL database?
// plain

The Python MySQL API provides a number of functions that can be used to interact with a MySQL database. To use the API in a Python program, it must first be imported using the `import` statement.

```
import mysql.connector
```

Once imported, a connection to the MySQL database can be established using the `connect()` function. This function requires parameters for the hostname, username, password, and database name.

```
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)
```

Once a connection is established, a cursor object can be created to execute SQL statements.

```
mycursor = mydb.cursor()
```

The `execute()` method of the cursor object can be used to execute SQL statements.

```
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

## Output example

```
(1, 'John', 'Highway 21')
(2, 'Peter', 'Lowstreet 4')
(3, 'Amy', 'Apple st 652')
(4, 'Hannah', 'Mountain 21')
(5, 'Michael', 'Valley 345')
(6, 'Sandy', 'Ocean blvd 2')
(7, 'Betty', 'Green Grass 1')
(8, 'Richard', 'Sky st 331')
(9, 'Susan', 'One way 98')
(10, 'Vicky', 'Yellow Garden 2')
(11, 'Ben', 'Park Lane 38')
(12, 'William', 'Central st 954')
(13, 'Chuck', 'Main Road 989')
(14, 'Viola', 'Sideway 1633')
```

The Python MySQL API also provides functions for creating, reading, updating, and deleting records from the database.

## Code explanation

1. `import mysql.connector` - imports the Python MySQL API
2. `mydb = mysql.connector.connect()` - establishes a connection to the MySQL database
3. `mycursor = mydb.cursor()` - creates a cursor object to execute SQL statements
4. `mycursor.execute()` - executes SQL statements
5. `mycursor.fetchall()` - retrieves the results of the SQL query

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I use the Python MySQL API to interact with a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-the-python-mysql-api-to-interact-with-a-mysql-database)