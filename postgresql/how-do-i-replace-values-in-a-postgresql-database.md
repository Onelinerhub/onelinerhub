# How do I replace values in a PostgreSQL database?
// plain

Replacing values in a PostgreSQL database is a fairly straightforward process. The following example code block shows how to replace a value in a PostgreSQL table:

```
UPDATE table_name
SET column_name = 'new_value'
WHERE condition;
```

Here, `table_name` is the name of the table, `column_name` is the name of the column, and `condition` is the condition that must be met for the value to be replaced. For example, if you wanted to replace the value of the `name` column in the `users` table with the value `John`, you would use the following code:

```
UPDATE users
SET name = 'John'
WHERE id = 1;
```

This code would replace the value of the `name` column in the `users` table for the row where `id` is equal to `1`.

## Code explanation


* `UPDATE` - This keyword is used to indicate that the values of one or more columns in a table should be updated.
* `users` - This is the name of the table.
* `SET` - This keyword is used to indicate which column should be updated and what its new value should be.
* `name = 'John'` - This is the column name and its new value.
* `WHERE` - This keyword is used to specify the condition that must be met for the value to be replaced.
* `id = 1` - This is the condition that must be met for the value to be replaced.

## Helpful links

* [PostgreSQL Documentation](https://www.postgresql.org/docs/9.3/sql-update.html)
* [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-update/)

onelinerhub: [How do I replace values in a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-replace-values-in-a-postgresql-database)