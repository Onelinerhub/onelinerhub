# How to remove all non-numeric characters using PHP regex?
// plain

To remove all non-numeric characters using PHP regex, the following code can be used:

```
$string = preg_replace('/[^0-9]/', '', $string);
```

This code will output a string with only numeric characters, for example:

```
Input: $string = "Hello123World456";
## Output example
 123456
```

The code consists of the following parts:

1. `preg_replace()` - This is a PHP function that performs a regular expression search and replace.
2. `/[^0-9]/` - This is the regular expression pattern that matches any non-numeric character.
3. `''` - This is the replacement string, which is an empty string in this case, meaning that the matched characters will be removed.
4. `$string` - This is the string that will be searched and replaced.

## Helpful links

- [PHP preg_replace() Function](https://www.w3schools.com/php/func_preg_replace.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to remove all non-numeric characters using PHP regex?](https://onelinerhub.com/php-regex/how-to-remove-all-non-numeric-characters-using-php-regex)