# How to get regex match in PHP?
// plain

Regex (Regular Expression) is a powerful tool used to match patterns in strings. In PHP, you can use the `preg_match()` function to get a regex match.

## Example code

```
$string = 'The quick brown fox jumps over the lazy dog.';
$pattern = '/quick (brown)(.*) jumps/';

if (preg_match($pattern, $string, $matches)) {
    echo 'Match found!';
    echo '<pre>';
    print_r($matches);
    echo '</pre>';
} else {
    echo 'No match found.';
}
```

## Output example

```
Match found!
Array
(
    [0] => quick brown fox jumps
    [1] => brown
    [2] => fox
)
```

## Code explanation

- `$string`: The string to search in.
- `$pattern`: The regex pattern to match.
- `preg_match()`: The function used to search for a match.
- `$matches`: An array containing the matches.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to get regex match in PHP?](https://onelinerhub.com/php-regex/how-to-get-regex-match-in-php)