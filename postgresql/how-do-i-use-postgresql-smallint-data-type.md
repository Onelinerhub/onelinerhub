# How do I use PostgreSQL smallint data type?
// plain

The PostgreSQL smallint data type is a 2-byte integer that can hold values between -32768 and 32767. It is useful for storing small numbers such as counts, ages, or other numerical values that will not exceed the range of a smallint.

## Example

```
CREATE TABLE my_table (
  id SERIAL PRIMARY KEY,
  age SMALLINT
);
```

This code creates a table called `my_table` with two columns, `id` and `age`. The `id` column is a serial data type which will auto-increment each time a new row is added to the table. The `age` column is a smallint data type and will store the age of the person associated with each row.

## Code explanation

1. `CREATE TABLE` - Creates a table in the database
2. `id SERIAL PRIMARY KEY` - Creates a column called `id` and sets it to auto-increment when a new row is added
3. `age SMALLINT` - Creates a column called `age` and sets it to the smallint data type

## Helpful links
- [PostgreSQL Documentation - Smallint](https://www.postgresql.org/docs/9.1/datatype-numeric.html#DATATYPE-SMALLINT)
- [PostgreSQL Documentation - CREATE TABLE](https://www.postgresql.org/docs/9.1/sql-createtable.html)

onelinerhub: [How do I use PostgreSQL smallint data type?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-smallint-data-type)