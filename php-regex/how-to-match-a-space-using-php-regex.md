# How to match a space using PHP regex?
// plain

To match a space using PHP regex, you can use the `\s` character class. This character class matches any whitespace character, including spaces, tabs, and line breaks.

## Example code

```php
$string = 'This is a string with a space.';
$pattern = '/\s/';

if (preg_match($pattern, $string)) {
    echo 'A space was found!';
}
```

## Output example

```
A space was found!
```

## Code explanation

- `$string`: This is a string variable containing the string to be searched.
- `$pattern`: This is a string variable containing the regular expression pattern to be used for the search. The `\s` character class is used to match any whitespace character, including spaces, tabs, and line breaks.
- `preg_match()`: This is a PHP function used to search a string for a pattern. It takes two parameters: the pattern to search for, and the string to search in.
- `echo`: This is a PHP statement used to output a string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions - Character Classes](https://www.regular-expressions.info/charclass.html)

onelinerhub: [How to match a space using PHP regex?](https://onelinerhub.com/php-regex/how-to-match-a-space-using-php-regex)