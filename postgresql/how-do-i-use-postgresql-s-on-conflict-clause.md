# How do I use PostgreSQL's ON CONFLICT clause?
// plain

The `ON CONFLICT` clause is a PostgreSQL extension to the SQL standard's `INSERT` statement. It allows the user to specify an alternative action to take when a unique constraint or primary key violation occurs.

## Example code

```sql
INSERT INTO table_name (column_name1, column_name2)
VALUES (value1, value2)
ON CONFLICT (column_name1) DO UPDATE SET column_name2 = value2;
```

This example will insert a row with `value1` and `value2` into `table_name`, unless a row with `value1` already exists in the `column_name1` column. In that case, the existing row will be updated with `value2`.

The `ON CONFLICT` clause can also take other actions, such as ignoring the row, or performing a custom function.

## Code explanation

* `INSERT INTO table_name (column_name1, column_name2)` - Inserts a row into the specified table, with the specified columns.
* `VALUES (value1, value2)` - Specifies the values to be inserted into the row.
* `ON CONFLICT (column_name1) DO UPDATE SET column_name2 = value2;` - Specifies what action to take if a row with `value1` already exists in the `column_name1` column.

## Helpful links
* [PostgreSQL Documentation - INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
* [PostgreSQL Documentation - ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT)

onelinerhub: [How do I use PostgreSQL's ON CONFLICT clause?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-on-conflict-clause)