# How can I use Python to yield results from a MySQL database?
// plain

Using Python to yield results from a MySQL database is a fairly simple process. The most important step is to install the appropriate Python library for interacting with MySQL. The most popular library for this purpose is MySQL Connector/Python.

Once the library is installed, the next step is to create a connection object. This object holds all the necessary information to connect to the MySQL database. The following code block demonstrates how to create a connection object:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)

# Output: <mysql.connector.connection.MySQLConnection object at 0x7f9f7d9b4eb8>
```

After the connection is established, a cursor object can be created. This object allows the user to execute SQL queries. The following code block demonstrates how to create a cursor object and execute a query:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Output:
# ('John', 'Highway 21')
# ('Peter', 'Lowstreet 4')
# ('Amy', 'Apple st 652')
# ('Hannah', 'Mountain 21')
```

## Code explanation


1. `import mysql.connector` - Imports the library for interacting with MySQL.
2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")` - Creates a connection object with the necessary information to connect to the MySQL database.
3. `mycursor = mydb.cursor()` - Creates a cursor object.
4. `mycursor.execute("SELECT * FROM customers")` - Executes a SQL query.
5. `myresult = mycursor.fetchall()` - Fetches all the results from the query.
6. `for x in myresult: print(x)` - Prints each result from the query.

## Helpful links

- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [Creating a MySQL Connection Object](https://www.w3schools.com/python/python_mysql_create_db.asp)
- [Executing SQL Queries](https://www.w3schools.com/python/python_mysql_select.asp)
- [Fetching Results from Queries](https://www.w3schools.com/python/python_mysql_getdata.asp)

onelinerhub: [How can I use Python to yield results from a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-yield-results-from-a-mysql-database)