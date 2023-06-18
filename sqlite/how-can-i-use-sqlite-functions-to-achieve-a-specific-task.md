# How can I use SQLite functions to achieve a specific task?
// plain

SQLite functions can be used to achieve a specific task by writing an SQL query. For example, to get all the records of a table named `users`:

```
SELECT * FROM users;
```

This will return all the records of the `users` table.

## Code explanation


- `SELECT`: a keyword used to specify which columns to return
- `*`: a wildcard used to select all columns
- `FROM`: a keyword used to specify from which table to select
- `users`: the name of the table from which to select

Other SQLite functions can be used to achieve other tasks. For example, to get the sum of all values in a `score` column of the `users` table:

```
SELECT SUM(score) FROM users;
```

This will return the sum of all values in the `score` column.

## Code explanation


- `SELECT`: a keyword used to specify which columns to return
- `SUM`: a function used to calculate the sum of a column
- `score`: the name of the column to sum
- `FROM`: a keyword used to specify from which table to select
- `users`: the name of the table from which to select

For more information on SQLite functions, please refer to the [SQLite documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How can I use SQLite functions to achieve a specific task?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-functions-to-achieve-a-specific-task)