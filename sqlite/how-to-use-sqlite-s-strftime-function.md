# How to use SQLite's strftime function?
// plain

The `strftime()` function in SQLite is used to format date and time values according to a specified format. It can be used in SELECT, UPDATE, and DELETE statements, as well as in clauses like WHERE and ORDER BY.

For example, to get the current date and time, you can use the following code:
```
SELECT strftime('%Y-%m-%d %H:%M:%S');
```

This will return the current date and time in the format `YYYY-MM-DD HH:MM:SS`:
```
2020-07-03 15:45:06
```

The `strftime()` function takes two parameters:

1. The format string, which is a combination of characters and conversion specifiers that define how the date and time values will be formatted.
2. An optional argument, which is a date/time string that will be formatted according to the format string.

Here are some of the most commonly used conversion specifiers:

- `%Y`: 4-digit year
- `%m`: 2-digit month
- `%d`: 2-digit day
- `%H`: Hour (24-hour clock)
- `%M`: Minute
- `%S`: Second

For more information about the `strftime()` function, see the [SQLite documentation](https://www.sqlite.org/lang_datefunc.html).

onelinerhub: [How to use SQLite's strftime function?](https://onelinerhub.com/sqlite/how-to-use-sqlite-s-strftime-function)