# How to replace strings using PHP regex?
// plain

PHP provides a powerful set of regular expression functions that can be used to replace strings.

```
$string = 'This is a string';
$pattern = '/string/';
$replacement = 'sentence';

echo preg_replace($pattern, $replacement, $string);
```

## Output example

```
This is a sentence
```

The code above uses the `preg_replace()` function to replace the string `string` with `sentence` in the variable `$string`. The `$pattern` variable contains the regular expression pattern to match the string to be replaced, and the `$replacement` variable contains the string to replace it with.

The `preg_replace()` function takes three parameters: the regular expression pattern, the replacement string, and the string to be searched. It returns the modified string.

## Helpful links

- [PHP Regular Expression Functions](https://www.php.net/manual/en/ref.regex.php)
- [PHP preg_replace() Function](https://www.w3schools.com/php/func_preg_replace.asp)

onelinerhub: [How to replace strings using PHP regex?](https://onelinerhub.com/php-regex/how-to-replace-strings-using-php-regex)