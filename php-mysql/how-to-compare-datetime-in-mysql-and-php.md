# How to compare datetime in MySQL and PHP?
// plain

MySQL and PHP both have built-in functions to compare datetime values.

In MySQL, the `DATE_SUB()` function can be used to compare two datetime values. It returns the difference between two datetime values in seconds.

```
SELECT DATE_SUB(datetime1, datetime2)
```

## Output example

```
-7200
```

In PHP, the `strtotime()` function can be used to compare two datetime values. It returns the difference between two datetime values in seconds.

```
$difference = strtotime($datetime1) - strtotime($datetime2);
```

## Output example

```
-7200
```

## Code explanation

- `DATE_SUB()`: MySQL function to compare two datetime values and return the difference in seconds
- `strtotime()`: PHP function to compare two datetime values and return the difference in seconds

## Helpful links
- [MySQL DATE_SUB() Function](https://www.w3schools.com/sql/func_mysql_date_sub.asp)
- [PHP strtotime() Function](https://www.w3schools.com/php/func_date_strtotime.asp)

onelinerhub: [How to compare datetime in MySQL and PHP?](https://onelinerhub.com/php-mysql/how-to-compare-datetime-in-mysql-and-php)