# How to get yesterday's date in Mariadb?
// plain

To get yesterday's date in Mariadb, you can use the `DATE_SUB` function. This function takes two parameters, the first being the date you want to subtract from, and the second being the interval you want to subtract.

## Example code

```
SELECT DATE_SUB(CURDATE(), INTERVAL 1 DAY);
```

## Output example

```
2020-09-17
```

## Code explanation

- `DATE_SUB`: This is the function used to subtract a date from another date.
- `CURDATE()`: This is a function that returns the current date.
- `INTERVAL 1 DAY`: This is the interval that is being subtracted from the current date.

## Helpful links
- [MySQL DATE_SUB Function](https://www.w3resource.com/mysql/date-and-time-functions/mysql-date_sub-function.php)

onelinerhub: [How to get yesterday's date in Mariadb?](https://onelinerhub.com/mariadb/how-to-get-yesterday-s-date-in-mariadb)