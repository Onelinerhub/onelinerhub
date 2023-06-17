# How do I store a float value in PostgreSQL?
// plain

In PostgreSQL, you can store floating point numbers in a column of type `real` or `double precision`.

For example, to create a table with a `real` column:
```sql
CREATE TABLE test_table (
  id serial PRIMARY KEY,
  value real
);
```

To insert a float value into the table:
```sql
INSERT INTO test_table (value) VALUES (3.14);
```

To retrieve the float value from the table:
```sql
SELECT value FROM test_table WHERE id = 1;
```

The output will be:
```
 value
-------
  3.14
(1 row)
```

- `real` and `double precision` columns can be used to store float values in PostgreSQL.
- `CREATE TABLE` is used to create a table with the desired columns.
- `INSERT` is used to insert float values into the table.
- `SELECT` is used to retrieve the float value from the table.

## Helpful links
- [PostgreSQL Documentation - Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [PostgreSQL Documentation - CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html)
- [PostgreSQL Documentation - INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
- [PostgreSQL Documentation - SELECT](https://www.postgresql.org/docs/current/sql-select.html)

onelinerhub: [How do I store a float value in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-store-a-float-value-in-postgresql)