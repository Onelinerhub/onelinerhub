# How to extract a group when using regex in PHP?
// plain

Regex (regular expressions) can be used to extract a group of characters from a string in PHP.

```
$string = 'This is a string';

preg_match('/This (.*) string/', $string, $matches);

echo $matches[1];
```

The output of the above code will be:

```
is a
```

## Code explanation


- `$string = 'This is a string';` - This is the string from which the group will be extracted.
- `preg_match('/This (.*) string/', $string, $matches);` - This is the regex expression used to extract the group. The `(.*)` part of the expression is the group that will be extracted.
- `echo $matches[1];` - This will output the extracted group.

## Helpful links

- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to extract a group when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-extract-a-group-when-using-regex-in-php)