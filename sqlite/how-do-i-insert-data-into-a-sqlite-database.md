# How do I insert data into a SQLite database?
// plain

To insert data into a SQLite database, follow the steps below:

1. Connect to the SQLite database using the `sqlite3` Python module.

```python
import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
```

2. Create a SQL statement to insert the data into the table.

```python
sql_statement = "INSERT INTO users (name, email) VALUES (?, ?)"
```

3. Execute the statement with the data to be inserted.

```python
cursor.execute(sql_statement, ("John Doe", "johndoe@example.com"))
```

4. Commit the changes to the database.

```python
connection.commit()
```

5. Close the connection to the database.

```python
connection.close()
```

For more information, see the [SQLite Documentation](https://www.sqlite.org/docs.html) and the [Python SQLite3 Tutorial](https://www.pythoncentral.io/introduction-to-sqlite-in-python/).

onelinerhub: [How do I insert data into a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-insert-data-into-a-sqlite-database)