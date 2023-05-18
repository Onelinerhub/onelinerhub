# How to use regex in PHP to do a case insensitive search?
// plain

To do a case insensitive search using regex in PHP, you can use the `i` modifier. This modifier will make the regex pattern case insensitive.

## Example code

```php
$string = 'Hello World';
$pattern = '/hello/i';

if (preg_match($pattern, $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

## Code explanation

- `$string`: This is the string that we are searching in.
- `$pattern`: This is the regex pattern that we are using to search. The `i` modifier makes it case insensitive.
- `preg_match()`: This is the function used to search for a pattern in a string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expression Modifiers](https://www.regular-expressions.info/modifiers.html)

onelinerhub: [How to use regex in PHP to do a case insensitive search?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-do-a-case-insensitive-search)