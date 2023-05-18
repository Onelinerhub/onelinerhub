# How to use PHP regex to match an exact string?
// plain

To match an exact string using PHP regex, you can use the `preg_match()` function. This function takes two parameters: the pattern to match and the string to search. The pattern should be enclosed in forward slashes (`/`).

For example, to match the exact string `Hello World`, you can use the following code:
```php
$string = 'Hello World';
$pattern = '/Hello World/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

The code above consists of the following parts:

1. `$string`: This is the string to search.
2. `$pattern`: This is the pattern to match. It should be enclosed in forward slashes (`/`).
3. `preg_match()`: This is the function used to match the pattern against the string. It takes two parameters: the pattern and the string.
4. `if` statement: This is used to check if the pattern matches the string. If it does, the code inside the `if` statement will be executed.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions (Regex)](https://www.w3schools.com/php/php_regex.asp)

onelinerhub: [How to use PHP regex to match an exact string?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-an-exact-string)