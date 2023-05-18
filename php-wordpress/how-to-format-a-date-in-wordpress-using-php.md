# How to format a date in WordPress using PHP?
// plain

The WordPress function `date_i18n()` can be used to format a date in WordPress using PHP. This function takes a timestamp as the first argument and a date format as the second argument.

```
echo date_i18n( 'F j, Y', time() );
```

The output of the above code will be something like `July 15, 2020`.

## Code explanation


- `date_i18n()`: This is the WordPress function used to format a date.
- `F j, Y`: This is the date format used in the example. `F` stands for the full month name, `j` stands for the day of the month without leading zeros, and `Y` stands for the 4-digit year.
- `time()`: This is the timestamp used in the example. It is the current timestamp.

## Helpful links

- [date_i18n() | WordPress Developer Resources](https://developer.wordpress.org/reference/functions/date_i18n/)
- [PHP date() Function](https://www.w3schools.com/php/func_date_date.asp)

onelinerhub: [How to format a date in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-format-a-date-in-wordpress-using-php)