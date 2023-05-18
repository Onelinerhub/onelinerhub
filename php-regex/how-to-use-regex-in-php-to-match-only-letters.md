# How to use regex in PHP to match only letters?
// plain

Regex (Regular Expressions) is a powerful tool used to match patterns in strings. In PHP, it can be used to match only letters.

## Example code

```
$string = 'Hello World!';
$pattern = '/[a-zA-Z]/';

if (preg_match($pattern, $string)) {
    echo 'Matched!';
}
```

## Output example

```
Matched!
```

## Code explanation

- `$string`: This is the string that we want to match against.
- `$pattern`: This is the regex pattern that we use to match against the string. In this case, it is `/[a-zA-Z]/`, which matches any letter from a to z, both lowercase and uppercase.
- `preg_match()`: This is the function that we use to match the string against the regex pattern. It takes two parameters, the regex pattern and the string.
- `echo`: This is the function that we use to output the result of the match.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use regex in PHP to match only letters?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-only-letters)