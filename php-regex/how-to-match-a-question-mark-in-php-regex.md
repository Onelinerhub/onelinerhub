# How to match a question mark in PHP regex?
// plain

To match a question mark in PHP regex, use the `\?` character. This will match a literal question mark, as opposed to a wildcard character.

## Example code

```php
$string = 'This is a string with a question mark?';
$pattern = '/\?/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string`: This is the string that we are searching for a match in.
- `$pattern`: This is the regular expression pattern that we are using to search for a match.
- `preg_match()`: This is the PHP function that we are using to search for a match. It takes two parameters: the regular expression pattern and the string to search in.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match a question mark in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-a-question-mark-in-php-regex)