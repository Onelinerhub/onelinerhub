# How do I store a bigint value in a PostgreSQL database?
// plain

To store a bigint value in a PostgreSQL database, you can use the `BIGINT` data type. This data type stores a signed 8-byte integer value.

For example, the following code block creates a table with a `BIGINT` column and inserts a value:
```
CREATE TABLE bigint_example (
  id BIGINT
);

INSERT INTO bigint_example (id) VALUES (9223372036854775807);
```

The output of the above code block would be:
```
INSERT 0 1
```

## Code explanation


1. `CREATE TABLE bigint_example (id BIGINT);` - This creates a table named `bigint_example` with a single column named `id` of type `BIGINT`.

2. `INSERT INTO bigint_example (id) VALUES (9223372036854775807);` - This inserts the value `9223372036854775807` into the `id` column of the `bigint_example` table.

## Helpful links

- [PostgreSQL Documentation - BIGINT](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-BIGINT)
- [PostgreSQL Documentation - INSERT](https://www.postgresql.org/docs/current/sql-insert.html)

onelinerhub: [How do I store a bigint value in a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-store-a-bigint-value-in-a-postgresql-database)