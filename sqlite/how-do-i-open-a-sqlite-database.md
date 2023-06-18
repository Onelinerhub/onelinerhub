# How do I open a SQLite database?
// plain

1. To open a SQLite database, you need to use the `sqlite3` module of Python.
2. To connect to an existing database, the `connect()` method of the `sqlite3` module is used.
3. The syntax for `connect()` is as follows:
```
conn = sqlite3.connect('database_name.db')
```
4. If the database does not exist, a new database will be created using the given name.
5. Once the connection is established, you can create tables, insert data, and perform various operations using SQL commands.
6. To execute a single SQL command, the `execute()` method is used. The syntax for `execute()` is as follows:
```
cursor.execute('SQL command')
```
7. After all the operations are performed, you need to close the connection using the `close()` method. The syntax for `close()` is as follows:
```
conn.close()
```

## Helpful links
- [SQLite3 Python Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite3 Tutorial](https://www.sqlitetutorial.net/sqlite-python/)

onelinerhub: [How do I open a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-open-a-sqlite-database)