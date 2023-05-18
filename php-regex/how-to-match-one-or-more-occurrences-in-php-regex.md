# How to match one or more occurrences in PHP regex?
// plain

To match one or more occurrences in PHP regex, the `+` quantifier can be used. This quantifier matches one or more of the preceding character, group, or character class.

For example, the following code will match one or more occurrences of the letter `a`:
```php
$string = 'aabbcc';
preg_match('/a+/', $string, $matches);
```
The output of the above code will be:
```
Array
(
    [0] => aa
)
```

The code consists of the following parts:

- `$string = 'aabbcc';` - This is the string that will be searched for matches.
- `preg_match('/a+/', $string, $matches);` - This is the regular expression that will be used to search for matches. The `+` quantifier is used to match one or more occurrences of the preceding character, in this case `a`.
- `$matches` - This is the array that will contain the matches found by the regular expression.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match one or more occurrences in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-one-or-more-occurrences-in-php-regex)