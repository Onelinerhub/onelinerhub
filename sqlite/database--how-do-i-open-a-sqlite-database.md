# database

How do I open a SQLite database?
// plain

You can open a SQLite database using the `sqlite3` command line tool. To open a database, you need to specify the path to the database file.

For example:
```
$ sqlite3 mydatabase.sqlite
```
This will open the `mydatabase.sqlite` database file.

Once the database is open, you can use the following commands to interact with the database:

- `.tables`: List all tables in the database
- `.schema`: Show the schema of the database
- `.quit`: Quit the sqlite3 command line tool

You can also execute SQL statements to interact with the database. For example:

```
sqlite> SELECT * FROM users;

id | name | email
---|------|------
1  | John | john@example.com
2  | Jane | jane@example.com

sqlite>
```

For more information about the `sqlite3` command line tool, please refer to the [SQLite documentation](https://www.sqlite.org/cli.html).

onelinerhub: [database

How do I open a SQLite database?](https://onelinerhub.com/sqlite/database--how-do-i-open-a-sqlite-database)