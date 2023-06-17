# data types

How can I use Postgresql numeric data types to store numerical values?
// plain

PostgreSQL provides a variety of numeric data types for storing numerical values. These include:

- `SMALLINT`: Stores small integers in a 2-byte signed integer format.
- `INTEGER`: Stores larger integers in a 4-byte signed integer format.
- `BIGINT`: Stores very large integers in an 8-byte signed integer format.
- `DECIMAL`: Stores exact decimal numbers with a user-defined precision and scale.
- `NUMERIC`: Stores exact decimal numbers with a user-defined precision and scale, similar to `DECIMAL`.
- `REAL`: Stores single-precision floating-point numbers in a 4-byte format.
- `DOUBLE PRECISION`: Stores double-precision floating-point numbers in an 8-byte format.

For example, to create a table with a column of type `INTEGER`, you can use the following code:

```sql
CREATE TABLE my_table (
    my_column INTEGER
);
```

This code will create a table named `my_table` with a single column named `my_column` of type `INTEGER`.

The following links provide more information on PostgreSQL numeric data types:
- https://www.postgresql.org/docs/9.5/datatype-numeric.html
- https://www.postgresql.org/docs/9.5/datatype.html

onelinerhub: [data types

How can I use Postgresql numeric data types to store numerical values?](https://onelinerhub.com/postgresql/data-types--how-can-i-use-postgresql-numeric-data-types-to-store-numerical-values)