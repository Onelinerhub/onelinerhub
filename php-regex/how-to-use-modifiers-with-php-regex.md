# How to use modifiers with PHP regex?
// plain

Using modifiers with PHP regex is a powerful way to customize the behavior of a regular expression. Modifiers can be used to change the way a pattern is matched, such as making it case-insensitive or allowing it to match multiple times.

## Example code

```
$pattern = '/foo/i';
$string = 'Foo Bar';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$pattern = '/foo/i';`: This line defines the pattern to be matched. The `/i` modifier makes the pattern case-insensitive.
- `$string = 'Foo Bar';`: This line defines the string to be matched against the pattern.
- `if (preg_match($pattern, $string)) {`: This line uses the `preg_match()` function to match the pattern against the string.
- `echo 'Match found!';`: This line prints a message if the pattern is matched.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)
- [PHP Regex Modifiers](https://www.php.net/manual/en/reference.pcre.pattern.modifiers.php)

onelinerhub: [How to use modifiers with PHP regex?](https://onelinerhub.com/php-regex/how-to-use-modifiers-with-php-regex)