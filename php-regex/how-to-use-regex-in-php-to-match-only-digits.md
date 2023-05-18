# How to use regex in PHP to match only digits?
// plain

Regex (regular expressions) is a powerful tool for matching patterns in strings. In PHP, you can use regex to match only digits with the `\d` character class.

## Example code

```
$string = '123abc456';

if (preg_match('/\d/', $string)) {
    echo 'The string contains digits.';
}
```

## Output example

```
The string contains digits.
```

## Code explanation

- `\d`: This is the character class for digits.
- `preg_match()`: This is the PHP function used to match a regex pattern against a string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match only digits?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-only-digits)