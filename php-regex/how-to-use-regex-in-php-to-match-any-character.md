# How to use regex in PHP to match any character?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. In PHP, it can be used to match any character using the `.` (dot) character.

```php
$string = 'Hello World!';
$pattern = '/H.llo/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string = 'Hello World!';` - This is the string we are searching in.
- `$pattern = '/H.llo/';` - This is the regex pattern we are using to search for. The `.` (dot) character is used to match any character.
- `preg_match($pattern, $string)` - This is the function used to search for the pattern in the string.
- `echo 'Match found!';` - This is the output when a match is found.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use regex in PHP to match any character?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-any-character)