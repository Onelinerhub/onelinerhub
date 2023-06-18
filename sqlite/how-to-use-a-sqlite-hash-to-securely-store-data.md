# How to use a SQLite hash to securely store data?
// plain

Using a SQLite hash to securely store data is a great way to keep your information safe. Here's an example of how to do it:

```
import sqlite3

# Connect to a database
conn = sqlite3.connect('example.db')

# Create a cursor
c = conn.cursor()

# Create a table with a hash column
c.execute('''CREATE TABLE users (name text, hash text)''')

# Insert a row of data
c.execute("INSERT INTO users VALUES ('John Smith', '6f8db599de986fab7a21625b7916589c')")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
```

This code creates a table called `users` with two columns, `name` and `hash`. It then inserts a row of data with the name `John Smith` and a hash of `6f8db599de986fab7a21625b7916589c`.

## Code explanation


1. `import sqlite3` - Imports the sqlite3 library.
2. `conn = sqlite3.connect('example.db')` - Connects to a database called `example.db`.
3. `c = conn.cursor()` - Creates a cursor to execute commands.
4. `c.execute('''CREATE TABLE users (name text, hash text)''')` - Creates a table called `users` with two columns, `name` and `hash`.
5. `c.execute("INSERT INTO users VALUES ('John Smith', '6f8db599de986fab7a21625b7916589c')")` - Inserts a row of data with the name `John Smith` and a hash of `6f8db599de986fab7a21625b7916589c`.
6. `conn.commit()` - Commits the changes made to the database.
7. `conn.close()` - Closes the connection.

## Helpful links

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [SQLite Python tutorial](https://www.sqlitetutorial.net/sqlite-python/)

onelinerhub: [How to use a SQLite hash to securely store data?](https://onelinerhub.com/sqlite/how-to-use-a-sqlite-hash-to-securely-store-data)