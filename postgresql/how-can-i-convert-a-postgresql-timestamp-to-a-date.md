# How can I convert a PostgreSQL timestamp to a date?
// plain

To convert a PostgreSQL timestamp to a date, you can use the `to_date` function. This function takes a timestamp as an argument and returns a date. For example:

```
SELECT to_date('2020-04-30 12:34:56', 'YYYY-MM-DD HH24:MI:SS')
```

## Output example

```
2020-04-30
```

The code above contains the following parts:
1. `SELECT`: This is a keyword used to select a value from a table.
2. `to_date`: This is the function used to convert a timestamp to a date.
3. `'2020-04-30 12:34:56'`: This is the timestamp argument passed to the `to_date` function.
4. `'YYYY-MM-DD HH24:MI:SS'`: This is the format of the timestamp argument.

For more information, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/current/functions-formatting.html).

onelinerhub: [How can I convert a PostgreSQL timestamp to a date?](https://onelinerhub.com/postgresql/how-can-i-convert-a-postgresql-timestamp-to-a-date)