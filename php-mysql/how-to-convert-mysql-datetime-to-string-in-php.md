# How to convert MySQL datetime to string in PHP?
// plain

To convert MySQL datetime to string in PHP, the `date()` function can be used. This function takes two parameters, the format of the output string and the timestamp. The timestamp can be obtained from the MySQL datetime field using the `strtotime()` function.

## Example code

```
$mysql_datetime = '2020-02-14 10:00:00';
$string_date = date('d-m-Y H:i:s', strtotime($mysql_datetime));
echo $string_date;
```

## Output example

```
14-02-2020 10:00:00
```

## Code explanation

- `date()`: This function takes two parameters, the format of the output string and the timestamp. It returns a string formatted according to the given format string using the given timestamp or the current local time if no timestamp is given.
- `strtotime()`: This function takes a string as a parameter and returns the corresponding timestamp.

## Helpful links
- [date()](https://www.php.net/manual/en/function.date.php)
- [strtotime()](https://www.php.net/manual/en/function.strtotime.php)

onelinerhub: [How to convert MySQL datetime to string in PHP?](https://onelinerhub.com/php-mysql/how-to-convert-mysql-datetime-to-string-in-php)