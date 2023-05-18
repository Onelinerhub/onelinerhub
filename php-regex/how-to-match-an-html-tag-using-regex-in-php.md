# How to match an HTML tag using regex in PHP?
// plain

Matching HTML tags using regex in PHP can be done using the `preg_match()` function. This function takes two parameters, the first being the regular expression pattern and the second being the string to match against.

```php
$html = '<p>This is a paragraph</p>';

if (preg_match('/<p>(.*?)<\/p>/', $html, $matches)) {
    echo $matches[1];
}
```

The output of the above code will be:

```
This is a paragraph
```

## Code explanation


- `preg_match()`: This is the PHP function used to match a regular expression pattern against a string.
- `/<p>(.*?)<\/p>/`: This is the regular expression pattern used to match an HTML paragraph tag. The `<p>` and `</p>` are the opening and closing tags, and the `.*?` is a wildcard that matches any character.
- `$matches`: This is an array that will contain the matches found by the regular expression.
- `echo $matches[1]`: This will output the contents of the first match found by the regular expression.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match an HTML tag using regex in PHP?](https://onelinerhub.com/php-regex/how-to-match-an-html-tag-using-regex-in-php)