# How do I create a table in SQLite?
// plain

To create a table in SQLite, you can use the `CREATE TABLE` statement. Here is an example of creating a table called `users` with two columns, `name` and `age`:
```
CREATE TABLE users (
  name TEXT,
  age INTEGER
);
```
This statement will create the table and no output will be generated.

The `CREATE TABLE` statement is composed of the following parts:
- `CREATE TABLE`: This is the keyword that tells SQLite to create a new table.
- `users`: This is the name of the table that is being created.
- `name TEXT`: This is the name of the first column, `name`, and its data type, `TEXT`.
- `age INTEGER`: This is the name of the second column, `age`, and its data type, `INTEGER`.

You can find more information about the `CREATE TABLE` statement in the [SQLite documentation](https://sqlite.org/lang_createtable.html).

onelinerhub: [How do I create a table in SQLite?](https://onelinerhub.com/sqlite/how-do-i-create-a-table-in-sqlite)