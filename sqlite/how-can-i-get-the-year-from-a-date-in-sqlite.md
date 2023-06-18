# How can I get the year from a date in SQLite?
// plain

To get the year from a date in SQLite, you can use the `strftime()` function. This function takes a date as an argument and returns a string based on the specified format. To get the year, you can use the `%Y` format specifier. For example:

```
SELECT strftime('%Y', '2020-07-15');
```

## Output example

```
2020
```

The code above uses the `strftime()` function with the `%Y` format specifier to get the year from the date '2020-07-15'.

## Code explanation


1. `strftime('%Y', '2020-07-15')` - This is the function call which takes the `%Y` format specifier and the date '2020-07-15' as arguments.

2. `%Y` - This is the format specifier which tells the `strftime()` function to return the year.

## Helpful links

- [SQLite strftime() Function](https://www.sqlitetutorial.net/sqlite-strftime/) - This link provides more information about the `strftime()` function and the different format specifiers.

onelinerhub: [How can I get the year from a date in SQLite?](https://onelinerhub.com/sqlite/how-can-i-get-the-year-from-a-date-in-sqlite)