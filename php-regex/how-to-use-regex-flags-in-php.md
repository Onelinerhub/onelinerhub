# How to use regex flags in PHP?
// plain

Regex flags are used to modify the behavior of a regular expression in PHP.

The most commonly used flags are `i` for case-insensitive matching, `m` for multiline matching, and `s` for dotall mode.

## Example code

```php
$pattern = '/^[a-z]$/i';
$string = 'A';

if (preg_match($pattern, $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$pattern`: The regular expression pattern to be used for matching.
- `$string`: The string to be matched against the pattern.
- `preg_match()`: The function used to match the string against the pattern.
- `/i`: The regex flag used to make the pattern case-insensitive.

## Helpful links
- [PHP Regex Flags](https://www.php.net/manual/en/reference.pcre.pattern.modifiers.php)
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use regex flags in PHP?](https://onelinerhub.com/php-regex/how-to-use-regex-flags-in-php)