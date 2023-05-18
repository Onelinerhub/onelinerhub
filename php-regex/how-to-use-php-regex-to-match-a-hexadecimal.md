# How to use PHP regex to match a hexadecimal?
// plain

Using PHP regex to match a hexadecimal is quite simple. The following example code block will match a hexadecimal string of any length:

```
$hexadecimal = preg_match('/^[0-9A-Fa-f]+$/', $string);
```

The output of the above code will be `1` if the string is a valid hexadecimal, and `0` if it is not.

## Code explanation


- `/^`: This is the start of the regular expression.
- `[0-9A-Fa-f]`: This is the character class that matches any hexadecimal character.
- `+`: This is a quantifier that matches one or more of the preceding character class.
- `$/`: This is the end of the regular expression.

## Helpful links

- [PHP Regular Expressions](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a hexadecimal?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-hexadecimal)