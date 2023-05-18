# How to use PHP regex to match URL?
// plain

Using PHP regex to match URL is a powerful way to validate and parse URLs. The following example code block shows how to use regex to match a URL:
```
$url = 'http://www.example.com/path/to/page.html';
$pattern = '/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/';

if(preg_match($pattern, $url)) {
    echo 'The URL is valid';
} else {
    echo 'The URL is not valid';
}
```
The output of the example code is:
```
The URL is valid
```
## Code explanation

- `$url`: a string containing the URL to be matched
- `$pattern`: a regex pattern to match the URL
- `preg_match()`: a PHP function to match a regex pattern against a string

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use PHP regex to match URL?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-url)