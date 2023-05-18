# How to use regex in PHP to match between two characters?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. In PHP, it can be used to match between two characters.

## Example code

```
$string = 'This is a string';
$pattern = '/[a-z]/';

if (preg_match($pattern, $string)) {
    echo 'Match found';
} else {
    echo 'No match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$string = 'This is a string';`: This is the string that we are searching in.
- `$pattern = '/[a-z]/';`: This is the regex pattern that we are using to search. The pattern `[a-z]` matches any character from a to z.
- `preg_match($pattern, $string)`: This is the function used to search for the pattern in the string.
- `if (preg_match($pattern, $string)) {`: This is the condition that checks if the pattern is found in the string.
- `echo 'Match found';`: This is the output if the pattern is found in the string.
- `echo 'No match found';`: This is the output if the pattern is not found in the string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match between two characters?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-between-two-characters)