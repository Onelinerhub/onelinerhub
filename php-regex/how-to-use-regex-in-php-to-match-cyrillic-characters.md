# How to use regex in PHP to match cyrillic characters?
// plain

To use regex in PHP to match cyrillic characters, you can use the `preg_match()` function. This function takes two parameters: a regular expression and a string to match against. The regular expression should include the cyrillic characters you want to match.

For example, to match any cyrillic characters, you can use the following code:

```php
$string = 'Привет, мир!';
if (preg_match('/[\p{Cyrillic}]/u', $string)) {
    echo 'Matched cyrillic characters!';
}
```

This will output:

```
Matched cyrillic characters!
```

The code consists of the following parts:

- `$string = 'Привет, мир!';` - this sets the string to match against.
- `preg_match('/[\p{Cyrillic}]/u', $string)` - this is the regular expression used to match cyrillic characters. The `/u` modifier is used to make the regular expression Unicode-aware.
- `echo 'Matched cyrillic characters!';` - this is the output when the regular expression matches.

For more information, see the [PHP documentation on preg_match()](https://www.php.net/manual/en/function.preg-match.php) and [Unicode character classes](https://www.regular-expressions.info/unicode.html).

onelinerhub: [How to use regex in PHP to match cyrillic characters?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-cyrillic-characters)