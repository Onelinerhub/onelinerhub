# How to remove non-printable characters using PHP regex?
// plain

Using PHP regex, non-printable characters can be removed from a string. The following example code block uses the `preg_replace` function to remove all non-printable characters from a string:

```
$string = preg_replace('/[\x00-\x1F\x7F]/u', '', $string);
```

This code will output a string with all non-printable characters removed:

```
This is a string with non-printable characters removed.

```

The code consists of the following parts:

- `preg_replace`: This is a PHP function used to perform a regular expression search and replace.
- `/[\x00-\x1F\x7F]/u`: This is the regular expression used to match all non-printable characters.
- `$string`: This is the string to be searched and replaced.

## Helpful links

- [PHP preg_replace](https://www.php.net/manual/en/function.preg-replace.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to remove non-printable characters using PHP regex?](https://onelinerhub.com/php-regex/how-to-remove-non-printable-characters-using-php-regex)