# How to use PHP regex with the "x" modifier?
// plain

The "x" modifier in PHP regex allows for comments and whitespace to be included in the pattern. This makes it easier to read and maintain complex regular expressions.

## Example code

```
$pattern = '/
    \b # Word boundary
    (
        \w+ # Match one or more word characters
    )
    \b # Word boundary
/x';

if (preg_match($pattern, 'Hello World', $matches)) {
    echo $matches[1];
}
```

## Output example

```
Hello
```

## Code explanation

- `\b`: Word boundary
- `\w+`: Match one or more word characters
- `/x`: The "x" modifier

Explanation:
- The `\b` word boundary is used to match the beginning and end of a word.
- The `\w+` matches one or more word characters.
- The `/x` modifier allows for comments and whitespace to be included in the pattern.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [PHP Regex Modifiers](https://www.php.net/manual/en/reference.pcre.pattern.modifiers.php)

onelinerhub: [How to use PHP regex with the "x" modifier?](https://onelinerhub.com/php-regex/how-to-use-php-regex-with-the--x--modifier)