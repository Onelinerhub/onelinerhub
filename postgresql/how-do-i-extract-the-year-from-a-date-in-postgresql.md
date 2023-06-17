# How do I extract the year from a date in PostgreSQL?
// plain

The easiest way to extract the year from a date in PostgreSQL is to use the `EXTRACT` function. This function takes a date field and a unit of time, and returns the corresponding value. For example, to extract the year from a date field called `date_field`, the following query can be used:

```
SELECT EXTRACT(YEAR FROM date_field) FROM table_name;
```

This will return a list of years for each of the dates in the `date_field` column.

The parts of this query are:
- `SELECT` - this is the clause used to indicate that data is being selected from a table.
- `EXTRACT` - this is the function used to extract the year from a date field.
- `YEAR` - this is the unit of time that is being extracted from the date field.
- `FROM` - this is the clause used to indicate the table that the data is being selected from.

## Helpful links
- https://www.postgresql.org/docs/9.1/functions-datetime.html
- https://www.postgresql.org/docs/9.1/sql-select.html

onelinerhub: [How do I extract the year from a date in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-extract-the-year-from-a-date-in-postgresql)