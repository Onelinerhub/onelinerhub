# How do I use SQLite data types in my software development project?
// plain

SQLite data types can be used in software development projects to store and manipulate data. For example, a table can be created with the following code block:

```
CREATE TABLE IF NOT EXISTS example_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
```

The code above creates a table named `example_table` with three columns: `id`, `name`, and `age`. The `id` column is an `INTEGER` data type and is set as the primary key. The `name` column is a `TEXT` data type, and the `age` column is also an `INTEGER` data type.

To insert data into the table, the `INSERT` statement can be used. For example:

```
INSERT INTO example_table (name, age)
VALUES ('John', 25);
```

This code inserts a row into the `example_table` with `name` set to `John` and `age` set to `25`.

Other SQLite data types that can be used in software development projects include `REAL`, `BLOB`, `NULL`, `NUMERIC`, `VARCHAR`, and `BOOLEAN`.

For more information on SQLite data types, please refer to the following links:

- [SQLite Data Types](https://www.sqlite.org/datatype3.html)
- [SQLite Data Types and Storage Classes](https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm)

onelinerhub: [How do I use SQLite data types in my software development project?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-data-types-in-my-software-development-project)