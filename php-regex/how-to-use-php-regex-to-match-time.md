# How to use PHP regex to match time?
// plain

PHP regex can be used to match time by using the `preg_match()` function. This function takes two parameters, the first being the regular expression pattern and the second being the string to match against.

```
$pattern = '/^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/';
$string = '12:30';

if (preg_match($pattern, $string)) {
    echo 'Time matched!';
}
```

## Output example

```
Time matched!
```

## Code explanation

- `$pattern`: This is the regular expression pattern used to match the time. It matches any time in the 24-hour format (e.g. 12:30).
- `$string`: This is the string to match against.
- `preg_match()`: This is the function used to match the regular expression pattern against the string. It returns `true` if the pattern matches, and `false` otherwise.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match time?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-time)