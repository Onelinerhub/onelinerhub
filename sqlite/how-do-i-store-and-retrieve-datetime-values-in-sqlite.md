# How do I store and retrieve datetime values in SQLite?
// plain

SQLite provides several functions to store and retrieve datetime values.

The `strftime()` function can be used to store datetime values in a SQLite database. It takes a datetime value and a format string as arguments and returns a string containing the formatted date and time. For example:

```
SELECT strftime('%Y-%m-%d %H:%M:%S', 'now');

2020-08-18 11:08:30
```

The `date()` function can be used to retrieve datetime values from a SQLite database. It takes a string containing a formatted date and time and returns a datetime value. For example:

```
SELECT date('2020-08-18 11:08:30');

2020-08-18 11:08:30
```

## Code explanation


* `strftime()` - Function used to store datetime values in a SQLite database.
* `'now'` - Datetime value used as argument for the `strftime()` function.
* `'%Y-%m-%d %H:%M:%S'` - Format string used as argument for the `strftime()` function.
* `date()` - Function used to retrieve datetime values from a SQLite database.
* `'2020-08-18 11:08:30'` - String containing a formatted date and time used as argument for the `date()` function.

## Helpful links

* [SQLite strftime()](https://www.sqlite.org/lang_datefunc.html)
* [SQLite date()](https://www.sqlite.org/lang_datefunc.html)

onelinerhub: [How do I store and retrieve datetime values in SQLite?](https://onelinerhub.com/sqlite/how-do-i-store-and-retrieve-datetime-values-in-sqlite)