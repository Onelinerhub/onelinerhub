# How to use regex in PHP to extract matched values?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. It can be used in PHP to extract matched values from a string.

## Example

```
$string = 'This is a string';
$pattern = '/\w+/';

preg_match_all($pattern, $string, $matches);

print_r($matches);
```

## Output example

```
Array
(
    [0] => Array
        (
            [0] => This
            [1] => is
            [2] => a
            [3] => string
        )

)
```

## Code explanation

- `$string`: This is the string that we want to match against.
- `$pattern`: This is the regex pattern that we want to use to match against the string.
- `preg_match_all()`: This is the PHP function used to match the pattern against the string. It takes three parameters: the pattern, the string, and an array to store the matches.
- `print_r()`: This is the PHP function used to print out the matches.

## Helpful links
- [PHP Regex Documentation](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to extract matched values?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-extract-matched-values)