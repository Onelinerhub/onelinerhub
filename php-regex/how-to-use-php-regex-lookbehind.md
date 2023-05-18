# How to use PHP regex lookbehind?
// plain

PHP regex lookbehind is a feature of regular expressions that allows you to match a pattern only if it is preceded by another pattern. It is written as `(?<=pattern)` and is used to match a pattern only if it is preceded by another pattern.

## Example code

```
$string = 'This is a string';
$pattern = '/(?<=This\s)is/';

if (preg_match($pattern, $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$string = 'This is a string';`: This is the string that we are searching in.
- `$pattern = '/(?<=This\s)is/';`: This is the regular expression pattern. The `(?<=This\s)` part is the lookbehind assertion, which means that the pattern will only match if it is preceded by the string `This `.
- `if (preg_match($pattern, $string)) {`: This is the condition that checks if the pattern matches the string.
- `echo 'Match found';`: This is the output that will be printed if the pattern matches the string.

## Helpful links
- [PHP Regex Lookbehind Tutorial](https://www.regular-expressions.info/lookaround.html)
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use PHP regex lookbehind?](https://onelinerhub.com/php-regex/how-to-use-php-regex-lookbehind)