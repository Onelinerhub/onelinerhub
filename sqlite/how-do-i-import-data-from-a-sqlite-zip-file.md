# How do I import data from a SQLite zip file?
// plain

1. Unzip the SQLite zip file.
2. Create a connection to the SQLite database using the `sqlite3` module.
   ```python
   import sqlite3
   conn = sqlite3.connect("my_database.db")
   ```
3. Create a cursor object to execute queries.
   ```python
   cursor = conn.cursor()
   ```
4. Use the `execute()` method to execute a SQL query.
   ```python
   cursor.execute("SELECT * FROM my_table")
   ```
5. Use the `fetchall()` method to fetch the results of the query.
   ```python
   results = cursor.fetchall()
   print(results)
   ```
   Output:
   ```
   [(1, 'John', 'Doe'), (2, 'Jane', 'Doe')]
   ```
6. Close the connection to the database.
   ```python
   conn.close()
   ```
7. Optionally, commit the changes to the database.
   ```python
   conn.commit()
   ```

## Helpful links
- [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How do I import data from a SQLite zip file?](https://onelinerhub.com/sqlite/how-do-i-import-data-from-a-sqlite-zip-file)