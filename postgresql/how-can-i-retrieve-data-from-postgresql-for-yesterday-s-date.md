# How can I retrieve data from PostgreSQL for yesterday's date?
// plain

The following example code block can be used to retrieve data from PostgreSQL for yesterday's date:

```
SELECT *
FROM table_name
WHERE date_column = CURRENT_DATE - INTERVAL '1 day';
```

This statement will select all data from the specified table with a date value equal to yesterday's date.

The parts of the code are:

1. `SELECT *` - This selects all columns from the specified table.
2. `FROM table_name` - This specifies the table from which the data should be retrieved.
3. `WHERE date_column = CURRENT_DATE - INTERVAL '1 day'` - This specifies the condition for selecting data from the table where the date column is equal to yesterday's date.

## Helpful links

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Date/Time Functions and Operators](https://www.postgresql.org/docs/9.5/functions-datetime.html)

onelinerhub: [How can I retrieve data from PostgreSQL for yesterday's date?](https://onelinerhub.com/postgresql/how-can-i-retrieve-data-from-postgresql-for-yesterday-s-date)