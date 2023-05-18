# How to use PHP regex to match special characters?
// plain

PHP regex can be used to match special characters using the `preg_match()` function.

```php
$string = 'This is a string with special characters!';

if (preg_match('/[^a-zA-Z0-9\s]/', $string)) {
    echo 'Special characters found!';
}
```

## Output example

```
Special characters found!
```

The code above uses the `preg_match()` function to check if the string contains any special characters. The regex pattern `/[^a-zA-Z0-9\s]/` is used to match any character that is not a letter, number, or whitespace.

- `preg_match()`: a PHP function used to match a regex pattern against a string
- `/[^a-zA-Z0-9\s]/`: a regex pattern used to match any character that is not a letter, number, or whitespace

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match special characters?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-special-characters)