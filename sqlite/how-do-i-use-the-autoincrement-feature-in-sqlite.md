# How do I use the autoincrement feature in SQLite?
// plain

Using the autoincrement feature in SQLite is easy. By including the keyword `AUTOINCREMENT` after the data type of a column, SQLite will automatically assign a unique integer to that column for each row in the table. For example:

```
CREATE TABLE test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
```

This will create a table with two columns, `id` and `name`. The `id` column will be an integer with a unique value for each row.

Here is an example of inserting a row into the table:

```
INSERT INTO test (name) VALUES ("John");
```

The output of this statement will be:

```
1 row affected
```

The `id` column will automatically be incremented to the next unique integer.

Here are some other useful links about using the autoincrement feature in SQLite:

- [SQLite Autoincrement](https://www.sqlitetutorial.net/sqlite-autoincrement/)
- [SQLite Autoincrement](https://www.tutorialspoint.com/sqlite/sqlite_autoincrement.htm)
- [SQLite Autoincrement](https://www.sqlite.org/autoinc.html)

onelinerhub: [How do I use the autoincrement feature in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-the-autoincrement-feature-in-sqlite)