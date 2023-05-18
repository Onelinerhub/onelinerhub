# How to use regex in PHP to match date in "yyyy-mm-dd" format?
// plain

The following regular expression can be used to match a date in the "yyyy-mm-dd" format in PHP:

```
$regex = '/^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/';
```

This expression will match a string of the form "yyyy-mm-dd" where:

- `[0-9]{4}`: The year is a 4-digit number
- `(0[1-9]|1[0-2])`: The month is a 2-digit number between 01 and 12
- `(0[1-9]|[1-2][0-9]|3[0-1])`: The day is a 2-digit number between 01 and 31

For example, the following code will return `true` if the date is in the correct format:

```
$date = '2020-04-30';
$regex = '/^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/';

if (preg_match($regex, $date)) {
    echo 'true';
}
```

## Output example

```
true
```

For more information about regular expressions in PHP, see the [PHP documentation](https://www.php.net/manual/en/book.pcre.php).

onelinerhub: [How to use regex in PHP to match date in "yyyy-mm-dd" format?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-date-in--yyyy-mm-dd--format)