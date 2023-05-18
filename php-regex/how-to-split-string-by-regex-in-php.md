# How to split string by regex in PHP?
// plain

Splitting a string by regex in PHP can be done using the `preg_split()` function.

```php
$string = 'This is a string';
$regex = '/\s+/';
$words = preg_split($regex, $string);

print_r($words);
```

The output of the above code will be:
```
Array
(
    [0] => This
    [1] => is
    [2] => a
    [3] => string
)
```

The `preg_split()` function takes two parameters:

1. `$regex` - The regular expression to use for splitting the string.
2. `$string` - The string to split.

The function will return an array of strings split by the regular expression.

## Helpful links

- [PHP preg_split() Function](https://www.w3schools.com/php/func_string_preg_split.asp)
- [PHP Regular Expressions](https://www.w3schools.com/php/php_regex.asp)

onelinerhub: [How to split string by regex in PHP?](https://onelinerhub.com/php-regex/how-to-split-string-by-regex-in-php)