# How to use PHP regex to match a hyphen?
// plain

To match a hyphen using PHP regex, you can use the `-` character. For example:

```php
$string = 'This-is-a-string';

if (preg_match('/-/', $string)) {
    echo 'Match found';
}
```

## Output example

```
Match found
```

The code above uses the `preg_match()` function to check if the `-` character is present in the string. If it is, it prints out `Match found`.

## Code explanation

- `$string = 'This-is-a-string';`: This is a string containing a hyphen.
- `preg_match('/-/', $string)`: This is the regex expression used to match the hyphen. The `-` character is used to match the hyphen.
- `echo 'Match found';`: This is the output printed when a match is found.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use PHP regex to match a hyphen?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-hyphen)