# How to match strings not containing a certain string in PHP regex?
// plain

To match strings not containing a certain string in PHP regex, use the `preg_match()` function with the `^` (caret) and `(?!string)` (negative lookahead) symbols. The `^` symbol indicates the start of the string, and the `(?!string)` symbol indicates that the string should not contain the specified string.

## Example code

```php
$string = "This is a string";

if (preg_match("/^(?!string)/", $string)) {
    echo "String does not contain 'string'";
}
```

## Output example

```
String does not contain 'string'
```

## Code explanation

- `preg_match()`: This is a PHP function used to perform a regular expression match.
- `^` (caret): This symbol indicates the start of the string.
- `(?!string)` (negative lookahead): This symbol indicates that the string should not contain the specified string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match strings not containing a certain string in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-strings-not-containing-a-certain-string-in-php-regex)