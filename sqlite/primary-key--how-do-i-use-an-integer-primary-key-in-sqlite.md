# primary key

How do I use an integer primary key in SQLite?
// plain

A primary key is a column or set of columns that uniquely identifies each row in a table. In SQLite, an integer primary key is a special type of column that is used to uniquely identify each row in a table. This is usually done by assigning a unique auto-incrementing integer to each row.

To use an integer primary key in SQLite, you need to specify the column as an INTEGER PRIMARY KEY when creating the table.

For example, the following code creates a table named "users" with an integer primary key column named "id":

```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

This will create a table with a "id" column that is an integer primary key. The "id" column will automatically be assigned a unique integer value for each row that is inserted into the table.

The following code inserts a row into the "users" table:

```
INSERT INTO users (name) VALUES ('John');
```

This will insert a row into the table with a unique integer value in the "id" column.

## Code explanation


- `CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL);`: This creates a table named "users" with an integer primary key column named "id".
- `INSERT INTO users (name) VALUES ('John');`: This inserts a row into the table with a unique integer value in the "id" column.

## Helpful links

- [SQLite Primary Key](https://www.sqlitetutorial.net/sqlite-primary-key/)
- [SQLite Autoincrement](https://www.sqlitetutorial.net/sqlite-autoincrement/)

onelinerhub: [primary key

How do I use an integer primary key in SQLite?](https://onelinerhub.com/sqlite/primary-key--how-do-i-use-an-integer-primary-key-in-sqlite)