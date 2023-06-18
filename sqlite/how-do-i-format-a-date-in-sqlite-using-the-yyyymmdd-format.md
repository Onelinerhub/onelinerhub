# How do I format a date in SQLite using the YYYYMMDD format?
// plain

To format a date in SQLite using the YYYYMMDD format, use the `strftime` function. The following example code block will return the current date in YYYYMMDD format:

```
SELECT strftime('%Y%m%d', 'now');
```

## Output example

```
20200831
```

The code above consists of two parts:
1. `strftime('%Y%m%d', 'now')` - This is the `strftime` function, which takes two arguments. The first argument is the format string, which specifies how the date should be formatted. The second argument is the date to be formatted. In this case, the date is set to `now`, which will return the current date.
2. `SELECT` - This keyword is used to query the database and return the result of the query.

## Helpful links
- [SQLite Documentation - Date and Time Functions](https://sqlite.org/lang_datefunc.html)
- [SQLite Tutorial - Date and Time](http://www.sqlitetutorial.net/sqlite-date/)

onelinerhub: [How do I format a date in SQLite using the YYYYMMDD format?](https://onelinerhub.com/sqlite/how-do-i-format-a-date-in-sqlite-using-the-yyyymmdd-format)