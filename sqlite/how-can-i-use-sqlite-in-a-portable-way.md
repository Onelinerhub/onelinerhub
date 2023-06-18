# How can I use SQLite in a portable way?
// plain

SQLite is an open-source, zero-configuration, serverless, transactional SQL database engine that is perfect for use in a portable way. It is a self-contained, embedded, full-featured, public-domain, SQL database engine.

To use SQLite in a portable way, you can create a database file in the same directory as your program and access it using the sqlite3 module. For example, the following code creates a database file called "mydb.db" and creates a table called "persons" with two columns:

```python
import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE persons
             (id int, name text)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
```

This code will create an empty database file called `mydb.db` in the same directory as the program. You can then use the `sqlite3` module to perform any database operations on the database file.

For more information, see the [SQLite documentation](https://www.sqlite.org/docs.html) and the [sqlite3 module documentation](https://docs.python.org/3/library/sqlite3.html).

onelinerhub: [How can I use SQLite in a portable way?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-in-a-portable-way)