# How do I use a SELECT statement to update a PostgreSQL table?
// plain

To update a PostgreSQL table using a SELECT statement, you must use the `UPDATE` command. The syntax is as follows:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

For example, if you wanted to update the `name` column of the `users` table to `John` for all records with an `id` of `1`, you could use the following query:

```sql
UPDATE users
SET name = 'John'
WHERE id = 1;
```

This would update the `name` column of the `users` table to `John` for all records with an `id` of `1`.

The parts of this query are as follows:

- `UPDATE` - the keyword used to inform the database that the query will be an update query
- `users` - the name of the table to be updated
- `SET` - the keyword used to inform the database of the columns and values to be updated
- `name = 'John'` - the column and value to be updated
- `WHERE` - the keyword used to inform the database of the condition that must be met in order for the update to take place
- `id = 1` - the condition that must be met in order for the update to take place

For more information on the `UPDATE` statement, see the [PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-update.html).

onelinerhub: [How do I use a SELECT statement to update a PostgreSQL table?](https://onelinerhub.com/postgresql/how-do-i-use-a-select-statement-to-update-a-postgresql-table)