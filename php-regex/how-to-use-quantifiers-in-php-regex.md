# How to use quantifiers in PHP regex?
// plain

Quantifiers are used in PHP regex to specify the number of times a character, group, or character class must appear in the input string for a match to be found.

For example, the following code uses the quantifier `+` to match one or more occurrences of the letter `a`:
```php
$string = 'aaabbb';
preg_match('/a+/', $string, $matches);
```
The output of the above code will be:
```
Array
(
    [0] => aaa
)
```

The following is a list of quantifiers and their meanings:

- `?` - matches zero or one occurrence of the preceding character, group, or character class
- `*` - matches zero or more occurrences of the preceding character, group, or character class
- `+` - matches one or more occurrences of the preceding character, group, or character class
- `{n}` - matches exactly `n` occurrences of the preceding character, group, or character class
- `{n,}` - matches `n` or more occurrences of the preceding character, group, or character class
- `{n,m}` - matches at least `n` and at most `m` occurrences of the preceding character, group, or character class

## Helpful links
- [PHP Regex Quantifiers](https://www.php.net/manual/en/regexp.reference.quantifiers.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use quantifiers in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-quantifiers-in-php-regex)