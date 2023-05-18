# How to use PHP regex to match a non-word?
// plain

Using PHP regex to match a non-word is possible with the `\W` character class. This character class matches any non-word character, which includes any character that is not a letter, number, or underscore.

## Example code

```php
$string = 'This is a string!';
$pattern = '/\W/';

preg_match_all($pattern, $string, $matches);

print_r($matches);
```

## Output example

```
Array
(
    [0] => Array
        (
            [0] =>
            [1] =>
            [2] => !
        )

)
```

## Code explanation

- `$string`: This is the string that we are searching through.
- `$pattern`: This is the regular expression pattern that we are using to search for non-word characters.
- `preg_match_all()`: This is the PHP function that we are using to search for matches in the string.
- `$matches`: This is the array that will contain all of the matches that are found.
- `print_r()`: This is the PHP function that we are using to print out the contents of the `$matches` array.

## Helpful links
- [PHP Regular Expression Functions](https://www.php.net/manual/en/ref.regex.php)
- [PHP preg_match_all() Function](https://www.w3schools.com/php/func_preg_match_all.asp)

onelinerhub: [How to use PHP regex to match a non-word?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-non-word)