# How to use curly braces in PHP regex?
// plain

Curly braces can be used in PHP regex to define a range of characters or numbers. For example, the following code block will match any string that contains a number between 0 and 5:

```
$regex = '/[0-5]/';
```

The output of this code will be `true` if the string contains a number between 0 and 5, and `false` otherwise.

## Code explanation


- `[0-5]`: This defines the range of characters or numbers that will be matched. In this case, it is any number between 0 and 5.

- `/`: This is the delimiter that marks the beginning and end of the regex.

- `$regex`: This is the variable that stores the regex.

## Helpful links

- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)

- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use curly braces in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-curly-braces-in-php-regex)