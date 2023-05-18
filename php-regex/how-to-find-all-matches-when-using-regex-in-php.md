# How to find all matches when using regex in PHP?
// plain

To find all matches when using regex in PHP, you can use the `preg_match_all()` function. This function takes two parameters: the regular expression pattern and the string to search. It returns an array of all matches found.

## Example code

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

- `$string`: The string to search.
- `$pattern`: The regular expression pattern.
- `preg_match_all()`: The function used to find all matches.
- `$matches`: The array of all matches found.
- `print_r()`: The function used to print the array of matches.

## Helpful links
- [PHP preg_match_all() Function](https://www.w3schools.com/php/func_preg_match_all.asp)
- [Regular Expressions](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to find all matches when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-find-all-matches-when-using-regex-in-php)