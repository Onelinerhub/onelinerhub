# How to get only numbers from a string using regex in PHP?
// plain

Using regex in PHP to get only numbers from a string is a simple task. The following example code block uses the `preg_match_all` function to extract all numbers from a string:

```
$string = 'This is a string with some numbers: 1, 2, 3, 4, 5';

preg_match_all('/\d+/', $string, $matches);

print_r($matches);
```

The output of the above code will be:

```
Array
(
    [0] => Array
        (
            [0] => 1
            [1] => 2
            [2] => 3
            [3] => 4
            [4] => 5
        )

)
```

## Code explanation


1. `$string = 'This is a string with some numbers: 1, 2, 3, 4, 5';` - This is the string from which the numbers will be extracted.

2. `preg_match_all('/\d+/', $string, $matches);` - This is the `preg_match_all` function which is used to extract all numbers from the string. The `\d+` is the regex pattern which matches all numbers.

3. `print_r($matches);` - This is used to print the extracted numbers.

## Helpful links

- [PHP preg_match_all() Function](https://www.w3schools.com/php/func_preg_match_all.asp)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to get only numbers from a string using regex in PHP?](https://onelinerhub.com/php-regex/how-to-get-only-numbers-from-a-string-using-regex-in-php)