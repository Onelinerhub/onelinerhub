# How to use an "or" condition in PHP regex?
// plain

An "or" condition in PHP regex can be used to match one of several possible patterns. For example, the following code block will match either the word "cat" or the word "dog":
```
$pattern = '/cat|dog/';
```
The output of this code will be either "cat" or "dog".

## Code explanation


1. `$pattern = '/`: This is the start of the regular expression.

2. `cat`: This is the first pattern to be matched.

3. `|`: This is the "or" operator, which allows for multiple patterns to be matched.

4. `dog`: This is the second pattern to be matched.

5. `/`: This is the end of the regular expression.

## Helpful links

- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use an "or" condition in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-an--or--condition-in-php-regex)