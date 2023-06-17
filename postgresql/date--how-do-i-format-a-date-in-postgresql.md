# date

How do I format a date in PostgreSQL?
// plain

The PostgreSQL `date` data type stores date and time values in the form of year, month, and day. To format a date in PostgreSQL, you can use the `to_char()` function. This function takes a date and a format string as arguments and returns a formatted string.

For example, the following code formats the date `2020-04-18` as `April 18, 2020`:
```
SELECT to_char(date '2020-04-18', 'Month DD, YYYY');
```

The output of this code is:
```
April 18, 2020
```

The code consists of two parts:
- The date value `date '2020-04-18'` is a literal date value.
- The format string `'Month DD, YYYY'` is a string that specifies how the date should be formatted. The format string consists of several elements, including `Month`, `DD`, and `YYYY` which represent the month, day, and year respectively.

For more information, see the PostgreSQL documentation on [Date/Time Functions and Operators](https://www.postgresql.org/docs/current/functions-datetime.html).

onelinerhub: [date

How do I format a date in PostgreSQL?](https://onelinerhub.com/postgresql/date--how-do-i-format-a-date-in-postgresql)