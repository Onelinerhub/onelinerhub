# How to use PHP regex to match a boolean value?
// plain

PHP regex can be used to match a boolean value by using the `preg_match()` function. This function takes two parameters, the first being the regular expression pattern and the second being the string to match against.

```
$string = 'true';
$pattern = '/^(true|false)$/';

if (preg_match($pattern, $string)) {
    echo 'Matched';
} else {
    echo 'Not matched';
}
```

## Output example

```
Matched
```

The code above uses the `preg_match()` function to match a boolean value. The first parameter is the regular expression pattern `/^(true|false)$/` which looks for either the string `true` or `false` at the beginning and end of the string. The second parameter is the string to match against, in this case `true`. If the string matches the pattern, the `preg_match()` function will return `true` and the `Matched` string will be printed. Otherwise, the `Not matched` string will be printed.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a boolean value?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-boolean-value)