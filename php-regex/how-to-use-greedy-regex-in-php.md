# How to use greedy regex in PHP?
// plain

Greedy regex is a powerful tool for pattern matching in PHP. It allows you to match a string of characters against a pattern and return the matches.

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

The code above uses the `preg_match_all()` function to match the pattern `\w+` against the string `This is a string`. The `\w+` pattern matches one or more word characters, which in this case are the words in the string. The `$matches` array contains the matches found by the pattern.

Parts of the code:
- `$string`: The string to be matched against the pattern.
- `$pattern`: The pattern to be used for matching.
- `preg_match_all()`: The function used to match the pattern against the string.
- `$matches`: The array containing the matches found by the pattern.

## Helpful links
- [PHP preg_match_all() Function](https://www.w3schools.com/php/func_preg_match_all.asp)
- [Regular Expressions (Regex) Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use greedy regex in PHP?](https://onelinerhub.com/php-regex/how-to-use-greedy-regex-in-php)