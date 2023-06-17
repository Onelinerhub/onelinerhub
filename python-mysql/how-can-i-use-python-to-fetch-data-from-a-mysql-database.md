# How can I use Python to fetch data from a MySQL database?
// plain

Python can be used to fetch data from a MySQL database using the `MySQLdb` module. The following example code block shows how to connect to a database, create a cursor, execute a query, and print the results:

```python
# Import the MySQLdb module
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="your_username", passwd="your_password", db="your_database")

# Create a cursor
cursor = db.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Print the results
for row in cursor.fetchall():
    print(row)
```

## Code explanation


1. `import MySQLdb`: This imports the `MySQLdb` module, which provides the functions needed to connect to and query a MySQL database.

2. `db = MySQLdb.connect(host="localhost", user="your_username", passwd="your_password", db="your_database")`: This establishes a connection to the database. The `host`, `user`, `passwd`, and `db` parameters are used to specify the hostname, username, password, and database name, respectively.

3. `cursor = db.cursor()`: This creates a cursor object, which is used to execute queries and fetch results.

4. `cursor.execute("SELECT * FROM your_table")`: This executes a query to select all records from the specified table.

5. `for row in cursor.fetchall():`: This loop iterates over the results of the query and prints each row.

For more information about using Python to connect to and query a MySQL database, see the following links:

- [MySQLdb User Guide](https://mysql-python.readthedocs.io/user_guide.html)
- [Python MySQL Tutorial](https://pynative.com/python-mysql-tutorial/)

onelinerhub: [How can I use Python to fetch data from a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-fetch-data-from-a-mysql-database)