# How to match the end of a string when using regex in PHP?
// plain

To match the end of a string when using regex in PHP, you can use the `$` character. This character is used to indicate the end of the string. For example:

```php
$string = 'This is a string';
$pattern = '/string$/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

The code above uses the `$` character to match the end of the string. The `$pattern` variable contains the regular expression `/string$/`, which looks for the string `string` at the end of the string. The `preg_match()` function is then used to check if the pattern matches the string. If a match is found, the `echo` statement is executed.

## Helpful links

- [PHP Regular Expression Functions](https://www.php.net/manual/en/ref.regex.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match the end of a string when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-match-the-end-of-a-string-when-using-regex-in-php)