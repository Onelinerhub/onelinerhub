# How do I resolve an error "no such column" when using SQLite?
// plain

To resolve an error "no such column" when using SQLite, you need to check the spelling of the column name and make sure the column exists in the table.

For example, if you have a table called `users` with columns `name` and `email`, and you write a query `SELECT age FROM users;`, you will get an error "no such column: age".

To fix this, you need to change the query to `SELECT name, email FROM users;`

The following code block shows an example of the query and its output:
```
SELECT name, email FROM users;

name         email
----------   ------------------------
John Doe     john.doe@example.com
Jane Doe     jane.doe@example.com
```

## Code explanation

- `SELECT`: the keyword used to select data from the table
- `name, email`: the columns to be selected from the table
- `FROM users`: the table from which to select the data

You can find more information about using SQLite in the [SQLite documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How do I resolve an error "no such column" when using SQLite?](https://onelinerhub.com/sqlite/how-do-i-resolve-an-error--no-such-column--when-using-sqlite)