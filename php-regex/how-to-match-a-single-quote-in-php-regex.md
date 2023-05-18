# How to match a single quote in PHP regex?
// plain

Single quotes can be matched in PHP regex using the `\` character. This is an escape character that allows you to match a single quote in a regex expression.

## Example code

```php
$string = 'This is a string with a single quote ' inside';
$pattern = '/\'/';

if (preg_match($pattern, $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$string`: This is the string that we are searching for a single quote in.
- `$pattern`: This is the regex pattern that we are using to search for a single quote. The `\` character is used to escape the single quote so that it can be matched.
- `preg_match()`: This is the PHP function that is used to search for a pattern in a string. It takes two parameters, the regex pattern and the string to search in.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions in PHP](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to match a single quote in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-a-single-quote-in-php-regex)