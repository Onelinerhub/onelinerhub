# How do I use the PostgreSQL row_number function?
// plain

The PostgreSQL row_number() function is used to assign a unique integer value to each row in a result set. This can be useful for pagination, ordering, and other operations.

## Example code

```
SELECT row_number() OVER (ORDER BY name) AS rn, name FROM customer;
```

## Output example

```
 rn |  name
----+--------
  1 | Alice
  2 | Bob
  3 | Charlie
```

## Code explanation

- `SELECT row_number()` - This is the function call. It assigns a unique integer value to each row.
- `OVER (ORDER BY name)` - This is an optional clause that specifies the order in which the row numbers should be generated. In this example, the rows are numbered in ascending order of the `name` column.
- `AS rn` - This is an optional clause that assigns an alias to the row number column. In this example, the row number column is named `rn`.
- `name FROM customer` - This is the source data. In this example, the row numbers are generated for the `name` column from the `customer` table.

## Helpful links
- [PostgreSQL Documentation: row_number()](https://www.postgresql.org/docs/9.5/functions-window.html#FUNCTIONS-WINDOW-ROW-NUMBER)

onelinerhub: [How do I use the PostgreSQL row_number function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-row-number-function)