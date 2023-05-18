# How to create a regex for a username in PHP?
// plain

A regular expression (regex) can be used to create a username in PHP. The following example code block will create a regex for a username that must be between 6 and 12 characters long and contain only lowercase letters and numbers:

```
$usernameRegex = '/^[a-z0-9]{6,12}$/';
```

The output of the example code will be a regex that can be used to validate a username:

```
/^[a-z0-9]{6,12}$/
```

## Code explanation


- `/`: This is the start and end delimiter of the regex.
- `^`: This is an anchor that matches the start of the string.
- `[a-z0-9]`: This is a character class that matches any lowercase letter or number.
- `{6,12}`: This is a quantifier that matches between 6 and 12 of the preceding character class.
- `$`: This is an anchor that matches the end of the string.

## Helpful links

- [Regular Expressions (Regex) Tutorial](https://www.regular-expressions.info/tutorial.html)
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to create a regex for a username in PHP?](https://onelinerhub.com/php-regex/how-to-create-a-regex-for-a-username-in-php)