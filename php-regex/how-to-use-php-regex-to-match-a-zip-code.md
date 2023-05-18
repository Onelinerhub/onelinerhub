# How to use PHP regex to match a zip code?
// plain

PHP regex can be used to match a zip code. The following example code block uses the `preg_match()` function to match a zip code with 5 digits:
```
$zip_code = '12345';
if (preg_match('/^\d{5}$/', $zip_code)) {
    echo 'Zip code is valid';
} else {
    echo 'Zip code is invalid';
}
```
The output of the example code is:
```
Zip code is valid
```
## Code explanation

- `/^\d{5}$/`: This is the regular expression used to match a zip code with 5 digits. The `^` and `$` symbols indicate the start and end of the string respectively, and `\d` matches any digit. The `{5}` indicates that the preceding character (`\d`) should be matched 5 times.
- `preg_match()`: This is the PHP function used to match a regular expression against a string. It takes two parameters: the regular expression and the string to match against.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a zip code?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-zip-code)