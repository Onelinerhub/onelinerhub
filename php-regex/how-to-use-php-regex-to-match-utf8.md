# How to use PHP regex to match UTF8?
// plain

PHP regex can be used to match UTF8 strings by using the `u` modifier. This modifier enables the pattern to be treated as a UTF-8 string.

## Example code

```
$string = 'This is a UTF-8 string';
$pattern = '/^This/u';

if (preg_match($pattern, $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$string`: This is the string that will be tested against the pattern.
- `$pattern`: This is the pattern that will be used to match the string. The `u` modifier is used to enable UTF-8 matching.
- `preg_match()`: This is the function used to match the string against the pattern.

## Helpful links
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)
- [UTF-8 and Unicode FAQ for Unix/Linux](https://www.cl.cam.ac.uk/~mgk25/unicode.html#utf-8)

onelinerhub: [How to use PHP regex to match UTF8?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-utf8)