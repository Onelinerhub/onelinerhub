# How do I check if a SQLite database exists?
// plain

To check if a SQLite database exists, you can use the following code:

```
import sqlite3

conn = sqlite3.connect('my_database.db')

if conn:
    print('Database exists')
```

This code will output `Database exists` if the database is found.

The code consists of the following parts:

1. `import sqlite3`: This imports the sqlite3 module, which is required to connect to the database.
2. `conn = sqlite3.connect('my_database.db')`: This creates a connection to the database located at `my_database.db`.
3. `if conn:`: This checks if the connection was successful.
4. `print('Database exists')`: This prints a message if the connection was successful.

## Helpful links

- [SQLite Python tutorial](https://www.sqlitetutorial.net/sqlite-python/)
- [SQLite Python API](https://docs.python.org/2/library/sqlite3.html)

onelinerhub: [How do I check if a SQLite database exists?](https://onelinerhub.com/sqlite/how-do-i-check-if-a-sqlite-database-exists)