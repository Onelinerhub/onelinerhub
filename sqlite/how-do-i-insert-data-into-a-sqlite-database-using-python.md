# How do I insert data into a SQLite database using Python?
// plain

Inserting data into a SQLite Database using Python is a simple process. The following example code will insert a record into the 'users' table of a SQLite database:

```
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("INSERT INTO users VALUES ('John', 'Doe', 'john@example.com')")

conn.commit()
conn.close()
```

The code above does the following:
1. Imports the sqlite3 module.
2. Connects to the 'example.db' database.
3. Creates a cursor object.
4. Executes an SQL statement to insert a record into the 'users' table.
5. Commits the changes to the database.
6. Closes the connection to the database.

## Helpful links
- [sqlite3 - Python Standard Library](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How do I insert data into a SQLite database using Python?](https://onelinerhub.com/sqlite/how-do-i-insert-data-into-a-sqlite-database-using-python)