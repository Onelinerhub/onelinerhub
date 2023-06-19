# How do I use the SQLite ZIP VFS to compress a database?
// plain

1. Create a database and connect to it using the `sqlite3` module:
   ```python
   import sqlite3
   conn = sqlite3.connect('mydb.db')
   ```
2. Register the ZIP VFS with SQLite:
   ```python
   conn.execute('pragma vfs_register(zipvfs);')
   ```
3. Create a ZIP archive of the database:
   ```python
   conn.execute('pragma zipvfs_save(mydb.zip);')
   ```
4. The database is now compressed in the ZIP archive.

## Code explanation

- `sqlite3`: A python module used to connect to a SQLite database.
- `conn.execute()`: A method used to execute SQLite commands.
- `pragma vfs_register`: A SQLite command used to register the ZIP VFS.
- `pragma zipvfs_save`: A SQLite command used to compress the database into a ZIP archive.

## Helpful links
- [SQLite ZIP VFS](https://www.sqlite.org/zipvfs.html)
- [Python SQLite3 Module](https://docs.python.org/3/library/sqlite3.html)

onelinerhub: [How do I use the SQLite ZIP VFS to compress a database?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-zip-vfs-to-compress-a-database)