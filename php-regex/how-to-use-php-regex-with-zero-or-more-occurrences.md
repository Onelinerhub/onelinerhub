# How to use PHP regex with zero or more occurrences?
// plain

Using regular expressions with zero or more occurrences in PHP is done using the `*` character. This character is used to indicate that the preceding character or group of characters can occur zero or more times. For example, the following code will match any string that contains the letter `a` zero or more times:

```php
$regex = '/a*/';
```

The output of this code will be `true` if the string contains the letter `a` zero or more times, and `false` if it does not.

## Code explanation


- `/` - This is the start of the regular expression.
- `a` - This is the character that we are looking for.
- `*` - This indicates that the preceding character can occur zero or more times.
- `/` - This is the end of the regular expression.

## Helpful links

- [PHP Regex](https://www.php.net/manual/en/book.regex.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex with zero or more occurrences?](https://onelinerhub.com/php-regex/how-to-use-php-regex-with-zero-or-more-occurrences)