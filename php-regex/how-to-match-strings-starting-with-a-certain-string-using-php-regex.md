# How to match strings starting with a certain string using PHP regex?
// plain

To match strings starting with a certain string using PHP regex, you can use the `preg_match()` function. This function takes two parameters: a regular expression pattern and a string to match against. The pattern should start with a caret (^) followed by the string you want to match. For example, to match strings starting with "Hello":

```
$string = "Hello World!";

if (preg_match("/^Hello/", $string)) {
    echo "String starts with 'Hello'";
}
```

## Output example

```
String starts with 'Hello'
```

The code above consists of the following parts:

1. `$string = "Hello World!";` - This assigns the string "Hello World!" to the variable `$string`.
2. `if (preg_match("/^Hello/", $string)) {` - This uses the `preg_match()` function to check if the string stored in `$string` starts with "Hello". The `^` character in the regular expression pattern indicates that the string should start with "Hello".
3. `echo "String starts with 'Hello'";` - This prints out a message if the string stored in `$string` starts with "Hello".
4. `}` - This closes the `if` statement.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match strings starting with a certain string using PHP regex?](https://onelinerhub.com/php-regex/how-to-match-strings-starting-with-a-certain-string-using-php-regex)