# How to use regex in PHP to match dot character?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. In PHP, it can be used to match dot character (`.`) by using the `preg_match()` function.

```
<?php
$string = 'This is a string with a dot character.';
$pattern = '/\./';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string`: This is the string that will be searched for the pattern.
- `$pattern`: This is the regex pattern used to match the dot character.
- `preg_match()`: This is the function used to match the pattern in the string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match dot character?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-dot-character)