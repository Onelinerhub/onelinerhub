# How to get the first match when using regex in PHP?
// plain

The `preg_match()` function in PHP can be used to get the first match when using regex.

```php
$string = 'The quick brown fox jumps over the lazy dog.';
$pattern = '/quick (\w+)/';
preg_match($pattern, $string, $matches);
echo $matches[0];
```

The output of the above code will be:
```
quick brown
```

## Code explanation


- `$string`: This is the string in which the regex pattern will be searched.
- `$pattern`: This is the regex pattern which will be used to search the string.
- `preg_match()`: This is the function which will be used to search the string for the regex pattern. It takes three parameters: the regex pattern, the string to search, and an array to store the matches.
- `$matches`: This is the array which will store the matches.
- `echo $matches[0]`: This will output the first match.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to get the first match when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-get-the-first-match-when-using-regex-in-php)