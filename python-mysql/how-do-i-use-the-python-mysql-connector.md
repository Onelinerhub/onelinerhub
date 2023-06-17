# How do I use the Python MySQL connector?
// plain

The Python MySQL connector is a library that allows you to connect to a MySQL database and perform queries and other operations. It is available on the [PyPI](https://pypi.org/project/mysql-connector-python/) website.

To use the Python MySQL connector, you need to install it using the `pip install mysql-connector-python` command.

Once the connector is installed, you can use it to connect to a MySQL database and perform queries. For example:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Fetch all results
myresult = mycursor.fetchall()

# Print the results
for x in myresult:
  print(x)

# Output:
# (1, 'John', 'Highway 21')
# (2, 'Peter', 'Lowstreet 4')
# (3, 'Amy', 'Apple st 652')
# (4, 'Hannah', 'Mountain 21')
# (5, 'Michael', 'Valley 345')
```

The code above:

1. Imports the MySQL connector library.
2. Connects to the MySQL database.
3. Creates a cursor.
4. Executes a query.
5. Fetches the results.
6. Iterates over the results and prints them.

For more information on how to use the Python MySQL connector, you can refer to the [official documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use the Python MySQL connector?](https://onelinerhub.com/python-mysql/how-do-i-use-the-python-mysql-connector)