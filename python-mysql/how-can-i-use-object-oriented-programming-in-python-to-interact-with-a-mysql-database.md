# How can I use object-oriented programming in Python to interact with a MySQL database?
// plain

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to store and manipulate data. In Python, you can use the `MySQLdb` module to interact with a MySQL database. Here is an example of how to use `MySQLdb` to connect to a MySQL database and execute a query:

```python
import MySQLdb

# Connect to the database
db = MySQLdb.connect("localhost", "user", "password", "database")

# Create a cursor
cursor = db.cursor()

# Execute a query
cursor.execute("SELECT * FROM table")

# Fetch the results
results = cursor.fetchall()

# Iterate through the results
for row in results:
    print(row)
```

This example code will connect to a MySQL database on the localhost, execute a query to select all the rows from a table, and print out the results.

## Code explanation


1. `import MySQLdb`: imports the `MySQLdb` module.
2. `db = MySQLdb.connect("localhost", "user", "password", "database")`: connects to a MySQL database on the localhost.
3. `cursor = db.cursor()`: creates a cursor object.
4. `cursor.execute("SELECT * FROM table")`: executes a query to select all the rows from a table.
5. `results = cursor.fetchall()`: fetches the results of the query.
6. `for row in results`: iterates through the results and prints them out.

For more information, see the [MySQLdb documentation](https://mysql-python.sourceforge.io/MySQLdb.html).

onelinerhub: [How can I use object-oriented programming in Python to interact with a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-object-oriented-programming-in-python-to-interact-with-a-mysql-database)