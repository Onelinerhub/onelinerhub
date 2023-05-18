# How to escape a slash when using regex in PHP?
// plain

To escape a slash when using regex in PHP, you can use the `preg_quote()` function. This function takes a string as an argument and returns a version of the string with all regex special characters escaped with a backslash.

For example:
```
$string = '$^.+*?|/';
echo preg_quote($string);
```

## Output example

```
\$\^\.\+\*\?\|\/
```

The `preg_quote()` function escapes the following characters: `. \ + * ? [ ^ ] $ ( ) { } = ! < > | : -`.

## Helpful links
- [PHP preg_quote() Function](https://www.w3schools.com/php/func_string_preg_quote.asp)

onelinerhub: [How to escape a slash when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-escape-a-slash-when-using-regex-in-php)