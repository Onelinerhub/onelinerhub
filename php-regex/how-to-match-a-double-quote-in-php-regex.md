# How to match a double quote in PHP regex?
// plain

To match a double quote in PHP regex, you can use the following code:

```
$string = 'This is a "string"';
$pattern = '/"(.*?)"/';

preg_match($pattern, $string, $matches);
```

The output of the above code will be:

```
Array
(
    [0] => "string"
    [1] => string
)
```

## Code explanation


- `$string`: This is the string that we are trying to match.
- `$pattern`: This is the regular expression pattern that we are using to match the double quote. The pattern `/"(.*?)"/` will match any double quote that is surrounded by other characters.
- `preg_match()`: This is the PHP function that is used to match the regular expression pattern against the string.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match a double quote in PHP regex?](https://onelinerhub.com/php-regex/how-to-match-a-double-quote-in-php-regex)