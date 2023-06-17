# How do I use a MySQL database with Python?
// plain

Using a MySQL database with Python involves using a library to make the connections. The most popular one is [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/).

The following example code shows how to connect to a MySQL database and run a query:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

This code will output the contents of the customers table:

```
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Amy', 'Apple st 652')
('Hannah', 'Mountain 21')
```

The code consists of the following parts:

1. `import mysql.connector` - imports the MySQL Connector/Python library.
2. `mydb = mysql.connector.connect(...)` - connects to the MySQL database using the provided parameters.
3. `mycursor = mydb.cursor()` - creates a cursor object to execute queries.
4. `mycursor.execute("SELECT * FROM customers")` - executes the query to select all records from the customers table.
5. `myresult = mycursor.fetchall()` - fetches all the results from the query.
6. `for x in myresult: print(x)` - iterates through the results and prints them.

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use a MySQL database with Python?](https://onelinerhub.com/python-mysql/how-do-i-use-a-mysql-database-with-python)