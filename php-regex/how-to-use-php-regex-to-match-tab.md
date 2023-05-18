# How to use PHP regex to match tab?
// plain

PHP regex can be used to match tab by using the `\t` character.

## Example code

```php
$string = "This\tis\ta\ttab";
$pattern = "/\t/";

if (preg_match($pattern, $string)) {
    echo "Match found!";
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string`: This is the string that will be searched for the tab character.
- `$pattern`: This is the regular expression pattern that will be used to search for the tab character.
- `preg_match()`: This is the PHP function used to search for a pattern in a string. It takes two parameters, the first being the pattern and the second being the string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use PHP regex to match tab?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-tab)