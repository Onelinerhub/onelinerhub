# How to set the time_zone in MySQL using PHP?
// plain

You can set the time_zone in MySQL using PHP by using the `date_default_timezone_set()` function.

## Example code

```
<?php
date_default_timezone_set('America/Los_Angeles');
?>
```

This code sets the timezone to America/Los_Angeles.

## Code explanation

- `date_default_timezone_set()` - This is the function used to set the timezone.
- `'America/Los_Angeles'` - This is the timezone that is being set.

## Helpful links
- [PHP date_default_timezone_set() Function](https://www.w3schools.com/php/func_date_date_default_timezone_set.asp)
- [List of Supported Timezones](https://www.php.net/manual/en/timezones.php)

onelinerhub: [How to set the time_zone in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-set-the-time_zone-in-mysql-using-php)