# How can I use SQLite with Python?
// plain

SQLite is a lightweight database that can be used with Python. To use SQLite with Python, you need to import the sqlite3 module.

```
import sqlite3
```

You can then create a connection to an SQLite database file, or you can create a new database file.

```
# Create a connection to a database file
conn = sqlite3.connect('example.db')

# Create a new database file
conn = sqlite3.connect('new_example.db')
```

Once you have a connection, you can create a cursor object and call its execute() method to run SQL commands.

```
# Create a cursor object
c = conn.cursor()

# Execute a SQL command
c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, grade INTEGER);")
```

You can also use the cursor's execute() method to insert, update, and delete data.

```
# Insert data
c.execute("INSERT INTO students VALUES ('John', 90);")

# Update data
c.execute("UPDATE students SET grade = 95 WHERE name = 'John';")

# Delete data
c.execute("DELETE FROM students WHERE name = 'John';")
```

Finally, you should commit the changes and close the connection.

```
# Commit changes
conn.commit()

# Close connection
conn.close()
```

## Helpful links
- [SQLite Python Tutorial](https://www.sqlitetutorial.net/sqlite-python/)
- [SQLite3 - Python Documentation](https://docs.python.org/3/library/sqlite3.html)

onelinerhub: [How can I use SQLite with Python?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-python)