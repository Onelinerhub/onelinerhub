# How to use PHP regex to match a line break?
// plain

To match a line break in PHP using regex, use the `\R` character class. This character class matches any line break sequence, including `\r`, `\n`, and `\r\n`.

## Example code

```php
$string = "This is a string
with a line break";

if (preg_match('/\R/', $string)) {
    echo "Line break found!";
}
```

## Output example

```
Line break found!
```

## Code explanation

- `\R`: The character class that matches any line break sequence.
- `preg_match()`: The function used to match a regular expression against a string.

## Helpful links
- [PHP Regular Expression Functions](https://www.php.net/manual/en/ref.regex.php)
- [Regular Expressions](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to use PHP regex to match a line break?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-line-break)