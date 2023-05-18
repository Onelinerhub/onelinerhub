# How to match a plus sign in PHP regex?
// plain

The plus sign `+` can be matched in PHP regex using the `\+` escape sequence.

```php
$string = 'This is a + sign';

if (preg_match('/\+/', $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

The `\+` escape sequence is used to match the literal `+` character in a regex pattern.

## Code explanation

- `\+`: escape sequence used to match the literal `+` character in a regex pattern

## Helpful links
- [PHP Regular Expression Syntax](https://www.php.net/manual/en/regexp.reference.escape.php)

onelinerhub: [How to match a plus sign in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-a-plus-sign-in-php-regex)