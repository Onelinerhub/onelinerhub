# How can I query a SQLite database for records from yesterday's date?
// plain

To query a SQLite database for records from yesterday's date, the following code can be used:

```
SELECT * FROM table_name
WHERE date = date('now', '-1 day');
```

This code will return all records from the table specified (`table_name`) that were added yesterday.

The code is composed of the following parts:
- `SELECT * FROM table_name`: This part of the code selects all records from the specified table.
- `WHERE date = date('now', '-1 day')`: This part of the code filters the results to only include records from yesterday's date.

For more information on using dates in SQLite, please refer to the [SQLite Documentation](https://www.sqlite.org/lang_datefunc.html).

onelinerhub: [How can I query a SQLite database for records from yesterday's date?](https://onelinerhub.com/sqlite/how-can-i-query-a-sqlite-database-for-records-from-yesterday-s-date)