# casting

How can I cast a year type in PostgreSQL?
// plain

Casting a year type in PostgreSQL can be done with the `CAST` function. This function takes an expression and a data type as parameters and returns the expression converted to the specified data type. For example, to cast a year type, you could use the following syntax:

```
SELECT CAST(year_column AS year) FROM table_name;
```

This will return the year_column column from the table_name table as a year type.

## Code explanation

- `SELECT`: the SQL keyword used to query data from a table
- `CAST`: the SQL function used to cast an expression to a specified data type
- `year_column`: the name of the column to be cast
- `AS year`: the target data type to cast the expression to
- `FROM table_name`: the name of the table where the column is located

## Helpful links
- [PostgreSQL Documentation - CAST](https://www.postgresql.org/docs/9.1/functions-formatting.html#FUNCTIONS-CONVERSION-CAST)

onelinerhub: [casting

How can I cast a year type in PostgreSQL?](https://onelinerhub.com/postgresql/casting--how-can-i-cast-a-year-type-in-postgresql)