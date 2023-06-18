# python

How can I use SQLite in Python?
// plain

SQLite is a lightweight database that can be used with Python. It is a great choice for applications that need a database but don't require a full-fledged database server such as MySQL or PostgreSQL. To use SQLite in Python, you need to import the `sqlite3` module.

## Example code

```
import sqlite3

# create a connection to the database
conn = sqlite3.connect('example.db')

# create a cursor
c = conn.cursor()

# execute a query
c.execute('SELECT * FROM table_name')

# fetch the results
results = c.fetchall()

# close the connection
conn.close()
```

The code above imports the `sqlite3` module and then creates a connection to the database, creates a cursor, executes a query, and fetches the results. Finally, it closes the connection.

## Code explanation

* `import sqlite3`: imports the `sqlite3` module which is used to interact with the SQLite database.
* `conn = sqlite3.connect('example.db')`: creates a connection to the database.
* `c = conn.cursor()`: creates a cursor which is used to execute queries.
* `c.execute('SELECT * FROM table_name')`: executes a query on the database.
* `results = c.fetchall()`: fetches the results of the query.
* `conn.close()`: closes the connection to the database.

## Helpful links
* [SQLite Official Documentation](https://www.sqlite.org/docs.html)
* [Python SQLite Tutorial](https://www.pythoncentral.io/introduction-to-sqlite-in-python/)

onelinerhub: [python

How can I use SQLite in Python?](https://onelinerhub.com/sqlite/python--how-can-i-use-sqlite-in-python)