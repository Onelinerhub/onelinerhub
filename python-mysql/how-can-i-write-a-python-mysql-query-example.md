# How can I write a Python MySQL query example?
// plain

To write a Python MySQL query example, you can use the `MySQLdb` module. This module provides an interface to the MySQL database server from Python.

Below is a simple example of how to execute a query using this module.

```python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","user","password","database")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
```

The output of this code would be:
```
Database version : 5.6.17
```

## Code explanation

- `import MySQLdb` - imports the MySQLdb module
- `db = MySQLdb.connect("localhost","user","password","database")` - connects to the MySQL server
- `cursor = db.cursor()` - creates a cursor object
- `cursor.execute("SELECT VERSION()")` - executes the SQL query
- `data = cursor.fetchone()` - fetches a single row from the result set
- `print "Database version : %s " % data` - prints the result from the query
- `db.close()` - closes the connection to the MySQL server

For more information, please see the [MySQLdb documentation](http://mysql-python.sourceforge.net/MySQLdb.html).

onelinerhub: [How can I write a Python MySQL query example?](https://onelinerhub.com/python-mysql/how-can-i-write-a-python-mysql-query-example)