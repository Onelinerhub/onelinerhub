# How to use regex in PHP to match any digit?
// plain

Regex (regular expressions) is a powerful tool for pattern matching in strings. In PHP, it can be used to match any digit with the `\d` character class.

## Example code

```
$string = 'This string contains 3 digits.';

if (preg_match('/\d/', $string)) {
    echo 'The string contains at least one digit.';
}
```

## Output example

```
The string contains at least one digit.
```

## Code explanation

- `\d`: character class that matches any digit
- `preg_match()`: PHP function that searches a string for a pattern and returns true if found

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match any digit?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-any-digit)