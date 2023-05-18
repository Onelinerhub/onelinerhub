# How to use word boundary in PHP regex?
// plain

Word boundary is a special character used in regular expressions to match the beginning or end of a word. In PHP, it is represented by the `\b` character.

## Example code

```php
$string = 'This is a test string';

if (preg_match('/\btest\b/', $string)) {
    echo 'Matched!';
}
```

## Output example

```
Matched!
```

## Code explanation

- `$string = 'This is a test string';`: This is the string we are searching in.
- `/\btest\b/`: This is the regular expression. The `\b` characters indicate that we are looking for the word "test" and not a substring of it.
- `preg_match('/\btest\b/', $string)`: This is the function call to `preg_match()` which searches for a match in the given string.
- `echo 'Matched!';`: This is the code that is executed if a match is found.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use word boundary in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-word-boundary-in-php-regex)