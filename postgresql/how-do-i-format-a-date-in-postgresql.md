# How do I format a date in PostgreSQL?
// plain

Formatting a date in PostgreSQL is a fairly straightforward process. The following example code block demonstrates how to format a date in PostgreSQL:

```
SELECT to_char(current_date, 'DD-Mon-YYYY') AS "Formatted Date";
```

The output of this code is:
```
Formatted Date
--------------
18-Aug-2020
```

This code formats the current date in the format of Day-Month-Year. The code is broken down into a few parts:
1. `SELECT`: This is the command used to retrieve data from the database.
2. `to_char(current_date, 'DD-Mon-YYYY')`: This is the function used to format the date. `current_date` is the date to be formatted and `'DD-Mon-YYYY'` is the format in which the date should be displayed.
3. `AS "Formatted Date"`: This is the alias given to the result of the query.

For more information on formatting dates in PostgreSQL, please refer to the following links:
- [PostgreSQL Documentation - Date/Time Functions and Operators](https://www.postgresql.org/docs/current/functions-formatting.html)
- [PostgreSQL Tutorial - Formatting Query Results](https://www.postgresqltutorial.com/formatting-query-results-in-postgresql/)

onelinerhub: [How do I format a date in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-format-a-date-in-postgresql)