# How to replace a tag using PHP regex?
// plain

Regex (Regular Expressions) can be used to replace tags in PHP.

```
$string = 'This is a <b>bold</b> string';
$string = preg_replace('/<b>(.*?)<\/b>/', '<strong>$1</strong>', $string);
```

The output of the above code will be:
```
This is a <strong>bold</strong> string
```

The code consists of three parts:
1. `$string` is the string that contains the tag to be replaced.
2. `preg_replace` is a PHP function that performs a regular expression search and replace. The first argument is the regular expression pattern to search for, the second argument is the replacement string, and the third argument is the string to search.
3. `$1` is a backreference to the first captured group in the regular expression pattern.

## Helpful links
- [PHP Regular Expression Functions](https://www.w3schools.com/php/php_ref_pcre.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to replace a tag using PHP regex?](https://onelinerhub.com/php-regex/how-to-replace-a-tag-using-php-regex)