# How to use PHP regex to match an XML tag?
// plain

PHP regex can be used to match an XML tag. The following example code block shows how to use regex to match an XML tag:
```
$string = '<tag>content</tag>';
$pattern = '/<(.+?)>(.*?)<\/(.+?)>/';
preg_match($pattern, $string, $matches);
```
The output of the example code is:
```
Array
(
    [0] => <tag>content</tag>
    [1] => tag
    [2] => content
    [3] => tag
)
```
## Code explanation

- `$string`: the string to be matched
- `$pattern`: the regex pattern used to match the string
- `preg_match()`: the PHP function used to match the string with the regex pattern

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)

onelinerhub: [How to use PHP regex to match an XML tag?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-an-xml-tag)