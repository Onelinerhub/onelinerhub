# How to use negative lookahead in PHP regex?
// plain

Negative lookahead is a powerful tool in PHP regex that allows you to match a pattern only if it is not followed by another pattern. It is written as `(?!pattern)` and is placed after the pattern you want to match.

For example, the following code will match any string that does not end with `ing`:
```php
$string = 'This is a test string';
$pattern = '/\w+(?!ing)$/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```
## Output example

```
Match found!
```

The code consists of the following parts:
- `$string`: The string to be matched.
- `$pattern`: The regular expression pattern. It consists of `\w+` which matches one or more word characters, followed by `(?!ing)` which is the negative lookahead assertion that matches only if the pattern is not followed by `ing`, and `$` which matches the end of the string.
- `preg_match()`: The PHP function used to match the pattern against the string.
- `echo`: The statement used to output the result.

## Helpful links
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)
- [Regular-Expressions.info - Lookahead and Lookbehind Zero-Length Assertions](https://www.regular-expressions.info/lookaround.html)

onelinerhub: [How to use negative lookahead in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-negative-lookahead-in-php-regex)