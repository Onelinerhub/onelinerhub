# How to use PHP regex to match letters, numbers and underscores?
// plain

Using PHP regex to match letters, numbers and underscores is a common task. The following example code block shows how to do this:

```
$string = 'abc123_ABC';
$pattern = '/^[a-zA-Z0-9_]+$/';

if (preg_match($pattern, $string)) {
    echo 'Matched!';
} else {
    echo 'Not matched!';
}
```

The output of the example code is:

```
Matched!
```

## Code explanation


- `$string = 'abc123_ABC';`: This is the string to be tested.
- `$pattern = '/^[a-zA-Z0-9_]+$/';`: This is the regular expression pattern used to match letters, numbers and underscores. The pattern `/^[a-zA-Z0-9_]+$/` means that the string should start with a letter, number or underscore, and end with a letter, number or underscore.
- `preg_match($pattern, $string)`: This is the function used to match the string against the pattern.
- `if (preg_match($pattern, $string)) {`: This is the condition used to check if the string matches the pattern.
- `echo 'Matched!';`: This is the output if the string matches the pattern.
- `echo 'Not matched!';`: This is the output if the string does not match the pattern.

## Helpful links

- [PHP Regular Expression Functions](https://www.w3schools.com/php/php_regex.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match letters, numbers and underscores?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-letters%2C-numbers-and-underscores)