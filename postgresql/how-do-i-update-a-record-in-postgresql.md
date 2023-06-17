# How do I update a record in PostgreSQL?
// plain

Updating a record in PostgreSQL is done using the `UPDATE` statement. The `UPDATE` statement is used to modify existing records in a table.

The syntax for the `UPDATE` statement is as follows:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Where `table_name` is the name of the table to update, `column1`, `column2`, etc. are the column names to update, `value1`, `value2`, etc. are the new values to set for the columns, and `condition` is the condition that must be met for the records to be updated.

For example, to update the `name` column in the `users` table for the user with `id` of 4, the following statement could be used:
```
UPDATE users
SET name = 'John Doe'
WHERE id = 4;
```

## Code explanation

- `UPDATE users` - specifies the table to update
- `SET name = 'John Doe'` - sets the `name` column to the specified value
- `WHERE id = 4` - specifies the condition that must be met for the records to be updated

## Helpful links
- [PostgreSQL Documentation - Update](https://www.postgresql.org/docs/current/sql-update.html)

onelinerhub: [How do I update a record in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-update-a-record-in-postgresql)