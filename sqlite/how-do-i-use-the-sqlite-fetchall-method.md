# How do I use the sqlite fetchall method?
// plain

The sqlite fetchall method is used to retrieve all rows of a query result in a single call. It returns a list of tuples containing all the rows of the query result. The syntax of the fetchall method is as follows:

```
cursor.fetchall()
```

The following example shows how to use the fetchall method to retrieve all the rows of a query result:

```
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Output:
# (1, 'John', 'Doe', 'john@example.com')
# (2, 'Jane', 'Doe', 'jane@example.com')
```

The code above:

1. Imports the `sqlite3` module.
2. Creates a connection to the database.
3. Creates a cursor object.
4. Executes a query to select all rows from the `employees` table.
5. Calls the `fetchall()` method to retrieve all rows of the query result.
6. Iterates over the rows and prints them.

## Helpful links

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Module Documentation](https://docs.python.org/3/library/sqlite3.html)

onelinerhub: [How do I use the sqlite fetchall method?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-fetchall-method)