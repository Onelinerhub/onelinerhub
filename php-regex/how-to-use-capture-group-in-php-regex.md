# How to use capture group in PHP regex?
// plain

Capture groups are used to group parts of a regular expression together and can be used to extract parts of a string. In PHP, capture groups are denoted by parentheses `()` and can be accessed using the `$matches` array.

## Example code

```php
$string = 'This is a string';
$pattern = '/This (is) a string/';
preg_match($pattern, $string, $matches);
```

## Output example

```
Array
(
    [0] => This is a string
    [1] => is
)
```

## Code explanation

- `$string`: The string to be matched against the regular expression.
- `$pattern`: The regular expression pattern, including capture groups denoted by parentheses `()`.
- `preg_match()`: The PHP function used to match a string against a regular expression pattern.
- `$matches`: The array that will contain the results of the match.

## Helpful links
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use capture group in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-capture-group-in-php-regex)