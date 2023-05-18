# How to use regex in PHP to match any character including newline?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. In PHP, it can be used to match any character including newline.

## Example code

```
$string = "This is a string
with a newline";

$pattern = "/^.*$/m";

if (preg_match($pattern, $string)) {
    echo "Match found!";
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string`: This is the string that we are trying to match.
- `$pattern`: This is the regex pattern that we are using to match the string. The `/m` modifier at the end of the pattern tells PHP to match the pattern across multiple lines.
- `preg_match()`: This is the PHP function used to match the pattern against the string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match any character including newline?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-any-character-including-newline)