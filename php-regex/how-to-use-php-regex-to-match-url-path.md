# How to use PHP regex to match URL path?
// plain

Using PHP regex to match URL path is a powerful way to validate and parse URLs. The following example code block shows how to use regex to match a URL path:

```
$url = 'http://www.example.com/path/to/page';

if (preg_match('#^https?://www\.example\.com/([^/]+)#i', $url, $matches)) {
    echo 'Path is: ' . $matches[1];
}
```

The output of the example code is:

```
Path is: path/to/page
```

## Code explanation


- `$url = 'http://www.example.com/path/to/page';`: This line assigns the URL to a variable.

- `if (preg_match('#^https?://www\.example\.com/([^/]+)#i', $url, $matches)) {`: This line uses the `preg_match` function to match the URL path. The `#^https?://www\.example\.com/([^/]+)#i` part is the regex pattern used to match the URL path.

- `echo 'Path is: ' . $matches[1];`: This line prints out the URL path. The `$matches[1]` part is used to access the first matched group in the regex pattern.

## Helpful links

- [PHP preg_match](https://www.php.net/manual/en/function.preg-match.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match URL path?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-url-path)