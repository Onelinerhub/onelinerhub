# How to match a quotation mark in PHP regex?
// plain

To match a quotation mark in PHP regex, you can use the `\` character before the quotation mark. This is known as an escape character and it tells the regex engine to treat the quotation mark as a literal character instead of a special character.

## Example code

```php
$string = 'This is a "test" string';
$pattern = '/".*"/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string = 'This is a "test" string';`: This is the string that we are searching for a match in.
- `$pattern = '/".*"/';`: This is the regex pattern that we are using to search for a match. The `\` character before the quotation mark tells the regex engine to treat the quotation mark as a literal character instead of a special character.
- `if (preg_match($pattern, $string)) {`: This is the condition that will be checked to see if a match is found.
- `echo 'Match found!';`: This is the code that will be executed if a match is found.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to match a quotation mark in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-a-quotation-mark-in-php-regex)