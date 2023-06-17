# How do I format a date in PostgreSQL?
// plain

PostgreSQL provides a variety of functions for formatting and manipulating dates and times. The most commonly used function for formatting dates is `to_char()`. This function takes a date, time, or timestamp as an argument and returns a formatted string.

For example, the following code block:
```
SELECT to_char(now(), 'DD Mon YYYY HH24:MI:SS')
```
will output the current date and time in the format `DD Mon YYYY HH24:MI:SS`, e.g. `08 Mar 2020 16:45:41`.

The syntax for `to_char()` is as follows: `to_char(date, format)`, where `date` is the date, time, or timestamp to be formatted and `format` is a string containing the desired format. The format string can contain a variety of characters, including `DD` for the day of the month, `Mon` for the month abbreviation, `YYYY` for the year, and `HH24` for the hour in 24-hour format.

In addition to `to_char()`, PostgreSQL provides several other functions for formatting and manipulating dates and times, such as `DATE_TRUNC()` for truncating a date to the nearest unit of time, `EXTRACT()` for extracting a specific part of a date, and `AGE()` for calculating the difference between two dates.

Further information about PostgreSQL date formatting can be found in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-formatting.html).

onelinerhub: [How do I format a date in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-format-a-date-in-postgresql-1686973131)