# constraint

How can I use a unique constraint with SQLite?
// plain

A unique constraint in SQLite is used to ensure that all values in a column are distinct from one another. This can be used to prevent duplicate entries in a table.

The syntax for creating a unique constraint in SQLite is as follows:

```
CREATE TABLE table_name (
    column1 datatype UNIQUE,
    column2 datatype,
    ...
);
```

For example, if we wanted to create a table called `users` with a unique constraint on the `username` column, the SQL statement would look like this:

```
CREATE TABLE users (
    username VARCHAR(255) UNIQUE,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
```

This would create a table called `users` with three columns: `username`, `first_name`, and `last_name`. The `username` column would have a unique constraint, meaning that all usernames must be distinct from one another.

The following SQL statement would then insert two rows into the `users` table. However, since the `username` column has a unique constraint, the second insert statement would fail since the `username` value is not unique:

```
INSERT INTO users (username, first_name, last_name) VALUES ('john_doe', 'John', 'Doe');
INSERT INTO users (username, first_name, last_name) VALUES ('john_doe', 'Jane', 'Doe');
```

The output of the above statements would be:

```
Query OK, 1 row affected (0.00 sec)
Error: UNIQUE constraint failed: users.username
```

### List of Code Parts

1. `CREATE TABLE table_name (column1 datatype UNIQUE, column2 datatype, ...);`: This statement creates a table with a unique constraint on the specified column.
2. `INSERT INTO users (username, first_name, last_name) VALUES ('john_doe', 'John', 'Doe');`: This statement inserts a row into the `users` table with the specified values.
3. `Error: UNIQUE constraint failed: users.username`: This is the output of the second insert statement, indicating that the `username` value is not unique and the statement failed.

### Relevant Links

- [SQLite UNIQUE Constraint](https://www.sqlitetutorial.net/sqlite-unique/)

onelinerhub: [constraint

How can I use a unique constraint with SQLite?](https://onelinerhub.com/sqlite/constraint--how-can-i-use-a-unique-constraint-with-sqlite)