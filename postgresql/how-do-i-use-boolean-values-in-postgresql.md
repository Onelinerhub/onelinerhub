# How do I use boolean values in PostgreSQL?
// plain

Boolean values are used in PostgreSQL to store true/false values. They are stored using the `boolean` data type.

## Example code

```
CREATE TABLE test (
    id serial PRIMARY KEY,
    is_active boolean NOT NULL DEFAULT false
);
```

This code creates a table called `test` with an `id` column of type `serial` and a `is_active` column of type `boolean`. The `is_active` column is set to `false` by default.

To insert data into the table, use the `INSERT` command:
```
INSERT INTO test (is_active) VALUES (true);
```

This code inserts a row into the `test` table with the `is_active` column set to `true`.

To query the table, use the `SELECT` command:
```
SELECT * FROM test WHERE is_active = true;
```

This code returns all rows from the `test` table where the `is_active` column is set to `true`.

## Helpful links
- [PostgreSQL Documentation on Boolean Data Type](https://www.postgresql.org/docs/9.1/datatype-boolean.html)
- [PostgreSQL Documentation on INSERT Command](https://www.postgresql.org/docs/9.1/sql-insert.html)
- [PostgreSQL Documentation on SELECT Command](https://www.postgresql.org/docs/9.1/sql-select.html)

onelinerhub: [How do I use boolean values in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-boolean-values-in-postgresql)