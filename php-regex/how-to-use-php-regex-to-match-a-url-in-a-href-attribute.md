# How to use PHP regex to match a URL in a href attribute?
// plain

To match a URL in a href attribute using PHP regex, you can use the following code:

```
$pattern = '/href="(.*?)"/';
$string = '<a href="http://example.com">Link</a>';

preg_match($pattern, $string, $matches);
```

The output of the code will be:

```
Array
(
    [0] => href="http://example.com"
    [1] => http://example.com
)
```

## Code explanation


- `$pattern`: This is the regular expression used to match the URL in the href attribute.
- `$string`: This is the string containing the HTML element with the href attribute.
- `preg_match()`: This is the PHP function used to match the regular expression against the string.

## Helpful links

- [PHP Regular Expression Functions](https://www.w3schools.com/php/php_regex.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a URL in a href attribute?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-url-in-a-href-attribute)