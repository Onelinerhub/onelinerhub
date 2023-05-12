# How to convert a MySQL timestamp to a datetime in PHP?
// plain

To convert a MySQL timestamp to a datetime in PHP, you can use the `strtotime()` function. This function takes a string as an argument and returns a Unix timestamp.

```
$timestamp = strtotime('2020-02-14 10:00:00');
echo date('Y-m-d H:i:s', $timestamp);
```

## Output example

```
2020-02-14 10:00:00
```

## Code explanation

- `strtotime()`: This function takes a string as an argument and returns a Unix timestamp.
- `date()`: This function takes two arguments, the format of the output and the timestamp.

## Helpful links
- [PHP strtotime() Function](https://www.w3schools.com/php/func_date_strtotime.asp)
- [PHP date() Function](https://www.w3schools.com/php/func_date_date.asp)

onelinerhub: [How to convert a MySQL timestamp to a datetime in PHP?](https://onelinerhub.com/php-mysql/how-to-convert-a-mysql-timestamp-to-a-datetime-in-php)