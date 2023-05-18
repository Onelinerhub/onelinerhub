# How to exclude a word when using regex in PHP?
// plain

To exclude a word when using regex in PHP, you can use the `preg_replace()` function. This function takes three parameters: the pattern to search for, the replacement string, and the subject string. The pattern should be a regular expression that uses the `^` character to exclude the word.

For example, to exclude the word "cat" from the string "The cat is in the hat", you can use the following code:
```
$string = "The cat is in the hat";
$pattern = "/^cat/";
$replacement = "";
$result = preg_replace($pattern, $replacement, $string);
echo $result;
```

The output of this code will be:
```
The is in the hat
```

The code consists of the following parts:
- `$string`: This is the subject string that will be searched.
- `$pattern`: This is the regular expression that will be used to search for the word. The `^` character is used to exclude the word.
- `$replacement`: This is the replacement string that will be used to replace the word. In this case, an empty string is used, so the word will be removed.
- `preg_replace()`: This is the function that will be used to perform the search and replace. It takes three parameters: the pattern, the replacement string, and the subject string.
- `echo $result`: This is used to output the result of the search and replace.

## Helpful links
- [PHP preg_replace() Function](https://www.w3schools.com/php/func_preg_replace.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to exclude a word when using regex in PHP?](https://onelinerhub.com/php-regex/how-to-exclude-a-word-when-using-regex-in-php)