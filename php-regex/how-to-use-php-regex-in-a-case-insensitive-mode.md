# How to use PHP regex in a case insensitive mode?
// plain

To use PHP regex in a case insensitive mode, you can use the `i` modifier. This modifier will make the regex match case insensitively.

For example:
```
$string = 'Hello World';
$pattern = '/hello/i';

if (preg_match($pattern, $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

The `i` modifier can be used with any regex pattern. It is placed after the closing `/` of the pattern.

## Code explanation

- `i` modifier: This modifier makes the regex match case insensitively.
- `preg_match()`: This function is used to match a regex pattern against a string.

## Helpful links
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)
- [PHP Regular Expression Syntax](https://www.php.net/manual/en/regexp.reference.syntax.php)

onelinerhub: [How to use PHP regex in a case insensitive mode?](https://onelinerhub.com/php-regex/how-to-use-php-regex-in-a-case-insensitive-mode)