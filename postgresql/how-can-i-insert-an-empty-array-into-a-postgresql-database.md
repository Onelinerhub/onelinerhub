# How can I insert an empty array into a PostgreSQL database?
// plain

To insert an empty array into a PostgreSQL database, you can use the `INSERT` statement with the `VALUES` clause. For example, the following code block inserts an empty array into the `mytable` table:

```
INSERT INTO mytable VALUES ('empty_array', ARRAY[]::integer[]);
```

This will insert a row with a column named `empty_array` and the value of the column will be an empty array of `integer` type.

## Code explanation


- `INSERT INTO mytable`: this is the statement used to insert a row into a table.
- `VALUES`: this clause is used to specify the values to be inserted.
- `ARRAY[]::integer[]`: this is the empty array of `integer` type.

## Helpful links

- [PostgreSQL Documentation: INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
- [PostgreSQL Documentation: Arrays](https://www.postgresql.org/docs/current/arrays.html)

onelinerhub: [How can I insert an empty array into a PostgreSQL database?](https://onelinerhub.com/postgresql/how-can-i-insert-an-empty-array-into-a-postgresql-database)