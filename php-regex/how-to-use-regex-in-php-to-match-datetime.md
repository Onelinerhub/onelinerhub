# How to use regex in PHP to match datetime?
// plain

Regex (Regular Expressions) can be used in PHP to match datetime. The following example code block shows how to use regex to match a datetime string in the format of `YYYY-MM-DD HH:MM:SS`:

```
$datetime = '2020-01-01 12:00:00';
$pattern = '/^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$/';

if (preg_match($pattern, $datetime, $matches)) {
    echo 'Matched!';
}
```

## Output example

```
Matched!
```

## Code explanation


- `$datetime = '2020-01-01 12:00:00';`: This is the datetime string to be matched.
- `$pattern = '/^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$/';`: This is the regex pattern used to match the datetime string. It consists of 6 parts, each part is enclosed in parentheses and matches a number of digits. The first part matches 4 digits, the second part matches 2 digits, and so on.
- `if (preg_match($pattern, $datetime, $matches)) {`: This is the condition to check if the datetime string matches the regex pattern. The `preg_match()` function takes the regex pattern and the datetime string as parameters and returns `true` if the datetime string matches the regex pattern.
- `echo 'Matched!';`: This is the code to be executed if the datetime string matches the regex pattern.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use regex in PHP to match datetime?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-match-datetime)