# How to use regex in PHP to match between two strings?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. In PHP, it can be used to match between two strings.

## Example code

```
$string1 = "Hello World";
$string2 = "Hello";

if (preg_match("/^$string2/", $string1)) {
    echo "Match found";
} else {
    echo "No match found";
}
```

## Output example

```
Match found
```

## Code explanation

- `$string1 = "Hello World";`: This is the first string to be matched.
- `$string2 = "Hello";`: This is the second string to be matched.
- `preg_match("/^$string2/", $string1)`: This is the regex expression used to match the two strings. The `^` symbol indicates that the match should start at the beginning of the string.
- `echo "Match found";`: This is the output when a match is found.
- `echo "No match found";`: This is the output when no match is found.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use regex in PHP to match between two strings?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-between-two-strings)