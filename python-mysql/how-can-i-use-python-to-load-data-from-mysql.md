# How can I use Python to load data from MySQL?
// plain

To load data from MySQL using Python, you can use the popular MySQL connector library. This library provides an API for connecting to and executing SQL queries on a MySQL database.

To use the library, you first need to install it. You can do this with the following command:
```
pip install mysql-connector-python
```

Once the library is installed, you can use the following code to connect to a MySQL database and execute a query:
```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Fetch the results
myresult = mycursor.fetchall()

# Print the results
print(myresult)
```

The output of the above code would be a list of tuples, each representing a row in the table:
```
[(1, 'John', 'Highway 21'),
 (2, 'Peter', 'Lowstreet 4'),
 (3, 'Amy', 'Apple st 652'),
 (4, 'Hannah', 'Mountain 21'),
 (5, 'Michael', 'Valley 345')]
```

The code consists of the following parts:

1. `import mysql.connector`: This imports the MySQL connector library.
2. `mydb = mysql.connector.connect()`: This creates a connection to the MySQL database using the provided credentials.
3. `mycursor = mydb.cursor()`: This creates a cursor object which can be used to execute queries.
4. `mycursor.execute()`: This executes a query on the database.
5. `myresult = mycursor.fetchall()`: This fetches the results of the query.
6. `print(myresult)`: This prints the results of the query.

For more information on using the MySQL Connector library, please refer to the [documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I use Python to load data from MySQL?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-load-data-from-mysql)