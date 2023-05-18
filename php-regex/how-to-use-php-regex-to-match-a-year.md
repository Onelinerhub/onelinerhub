# How to use PHP regex to match a year?
// plain

To use PHP regex to match a year, you can use the following code:
```
$year = preg_match('/\d{4}/', $string);
```
This will return `1` if the string contains a 4-digit year, or `0` if it does not.

The code consists of the following parts:
- `preg_match()`: This is a PHP function that performs a regular expression match.
- `/\d{4}/`: This is the regular expression pattern used to match a 4-digit year. The `\d` character class matches any digit, and the `{4}` quantifier specifies that exactly 4 digits must be matched.
- `$string`: This is the string that will be searched for a 4-digit year.

For more information on using regular expressions in PHP, see the [PHP documentation](https://www.php.net/manual/en/book.pcre.php).

onelinerhub: [How to use PHP regex to match a year?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-year)