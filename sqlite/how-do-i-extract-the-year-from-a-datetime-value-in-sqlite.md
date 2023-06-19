# How do I extract the year from a datetime value in SQLite?
// plain

To extract the year from a datetime value in SQLite, you can use the `strftime()` function. This function takes a datetime value as an argument and returns a string of the desired format. To extract the year, use the format specifier `%Y`, which will return the year as a 4-digit integer.

For example:
```
SELECT strftime('%Y', '2020-01-01 10:00:00');
```

## Output example

```
2020
```

The code above consists of the following parts:
* `SELECT` - specifies what should be returned from the query
* `strftime('%Y', '2020-01-01 10:00:00')` - the `strftime()` function, which takes a datetime value and returns the year as a 4-digit integer

## Helpful links
* [SQLite strftime() Function](https://www.sqlitetutorial.net/sqlite-strftime/)
* [SQLite Date and Time](https://www.sqlitetutorial.net/sqlite-date/)

onelinerhub: [How do I extract the year from a datetime value in SQLite?](https://onelinerhub.com/sqlite/how-do-i-extract-the-year-from-a-datetime-value-in-sqlite)