# How to use regex in PHP to match any string?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. It can be used in PHP to match any string.

## Example code

```
<?php
$string = 'This is a string';
$pattern = '/^.*$/';

if (preg_match($pattern, $string)) {
    echo 'Match found';
} else {
    echo 'No match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$string = 'This is a string';`: This is the string that we want to match.
- `$pattern = '/^.*$/';`: This is the regex pattern that we use to match the string. The `^` and `$` symbols indicate that the pattern should match the entire string. The `.*` part of the pattern matches any character (`.`) zero or more times (`*`).
- `preg_match($pattern, $string)`: This function is used to match the pattern against the string. It returns `true` if a match is found, and `false` otherwise.
- `if (preg_match($pattern, $string)) {`: This is an `if` statement that checks if the pattern matches the string.
- `echo 'Match found';`: This line is executed if the pattern matches the string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match any string?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-any-string)