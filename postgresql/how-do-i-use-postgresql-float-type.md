# How do I use PostgreSQL float type?
// plain

PostgreSQL float type is a data type used to store real numbers with precision up to 8 bytes. It is a variable precision type, which means that the actual number of bytes allocated to store the number depends on its value.

## Example code

```
CREATE TABLE float_example (
    id serial PRIMARY KEY,
    float_number float
);

INSERT INTO float_example (float_number)
VALUES (3.1415);

SELECT * FROM float_example;
```
## Output example

```
 id | float_number
----+--------------
  1 |       3.1415
(1 row)
```

In the example code above:
1. `CREATE TABLE float_example` creates a table called `float_example` with an `id` column of type `serial` as primary key and a `float_number` column of type `float`.
2. `INSERT INTO float_example` inserts a row into the table with a value of `3.1415` for the `float_number` column.
3. `SELECT * FROM float_example` retrieves all the records from the table.

## Helpful links

- [PostgreSQL Documentation - Float Type](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-FLOAT)
- [PostgreSQL Documentation - Data Types](https://www.postgresql.org/docs/current/datatype.html)

onelinerhub: [How do I use PostgreSQL float type?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-float-type)