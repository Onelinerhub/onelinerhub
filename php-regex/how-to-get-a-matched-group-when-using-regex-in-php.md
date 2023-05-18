# How to get a matched group when using regex in PHP?
// plain

To get a matched group when using regex in PHP, you can use the `preg_match()` function. This function takes two parameters: the regular expression pattern and the string to search. It returns an array of matches, or `FALSE` if no matches are found.

## Example code

```
$string = 'This is a string';
$pattern = '/\w+/';

preg_match($pattern, $string, $matches);

print_r($matches);
```

## Output example

```
Array
(
    [0] => This
    [1] => is
    [2] => a
    [3] => string
)
```

## Code explanation

- `$string`: This is the string to search.
- `$pattern`: This is the regular expression pattern to use.
- `preg_match()`: This is the function used to search the string for matches. It takes two parameters: the regular expression pattern and the string to search.
- `$matches`: This is the array that will contain the matches.
- `print_r()`: This is the function used to print the array of matches.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to get a matched group when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-get-a-matched-group-when-using-regex-in-php)