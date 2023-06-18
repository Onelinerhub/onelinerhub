# How do I create a SQLite file?
// plain

To create a SQLite file, you can use the `sqlite3` command line tool. The following example code will create a new database file called `my_database.db`:

```
sqlite3 my_database.db
```

The command will create a file in the current working directory. If the file already exists, the command will open the existing file instead.

To create a table in the database, you can use the `CREATE TABLE` statement. For example:

```
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);
```

This will create a table called `users` with two columns: `id` and `name`. The `id` column is an integer that is also the primary key for the table, and `name` is a text field that must not be empty.

You can also insert data into the table using the `INSERT` statement. For example:

```
INSERT INTO users (name) VALUES ('John Doe');
```

This will insert a new row into the `users` table with the name `John Doe`.

Finally, you can use the `SELECT` statement to query the data in the table. For example:

```
SELECT * FROM users;
```

This will return all rows in the `users` table.

## Helpful links

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/index.htm)

onelinerhub: [How do I create a SQLite file?](https://onelinerhub.com/sqlite/how-do-i-create-a-sqlite-file)