# How to use PHP regex to match a nbsp HTML whitespace?
// plain

PHP regex can be used to match a nbsp HTML whitespace by using the `\s` character class. This character class matches any whitespace character, including the nbsp HTML whitespace.

```php
$string = 'This is a string with&nbsp;a nbsp whitespace.';

if (preg_match('/\s/', $string)) {
    echo 'Matched whitespace!';
}
```

## Output example

```
Matched whitespace!
```

## Code explanation

- `\s`: character class that matches any whitespace character, including the nbsp HTML whitespace
- `preg_match()`: PHP function that searches a string for a pattern, and returns true if the pattern exists, and false otherwise

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to use PHP regex to match a nbsp HTML whitespace?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-nbsp-html-whitespace)