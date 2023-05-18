# How to use PHP regex with a variable in a pattern?
// plain

Using PHP regex with a variable in a pattern is quite simple. You can use the `preg_match()` function to match a pattern with a variable.

For example:
```
$string = 'Hello World';
$pattern = '/^Hello/';

if (preg_match($pattern, $string)) {
    echo 'The string starts with "Hello"';
}
```

## Output example

```
The string starts with "Hello"
```

The code above consists of the following parts:

1. `$string` - a variable containing the string to be matched
2. `$pattern` - a variable containing the pattern to be matched
3. `preg_match()` - a function that takes two parameters, the pattern and the string, and returns true if the pattern matches the string
4. `echo` - a statement that prints the output

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to use PHP regex with a variable in a pattern?](https://onelinerhub.com/php-regex/how-to-use-php-regex-with-a-variable-in-a-pattern)