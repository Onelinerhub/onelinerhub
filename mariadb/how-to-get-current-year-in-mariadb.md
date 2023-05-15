# How to get current year in Mariadb?
// plain

The current year can be obtained in Mariadb using the `YEAR()` function.

## Example code

```
SELECT YEAR(NOW());
```

## Output example

```
2020
```

The `YEAR()` function takes a date as an argument and returns the year of that date. In the example above, the `NOW()` function is used to get the current date and time, and the `YEAR()` function is used to get the current year.

## Code explanation

- `YEAR()`: Function to get the year of a given date
- `NOW()`: Function to get the current date and time

## Helpful links
- https://mariadb.com/kb/en/library/year/

onelinerhub: [How to get current year in Mariadb?](https://onelinerhub.com/mariadb/how-to-get-current-year-in-mariadb)