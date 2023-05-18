# How to remove a tag from a string using PHP regex?
// plain

Using PHP regex, you can remove a tag from a string by using the `preg_replace()` function. This function takes two parameters, the first being the pattern to search for and the second being the replacement string.

For example, to remove a tag from a string, you can use the following code:
```
$string = '<p>This is a string with a tag.</p>';
$string = preg_replace('/<[^>]*>/', '', $string);
```
The code above will search for any tag in the string and replace it with an empty string. The output of the code above will be:
```
This is a string with a tag.
```

The code consists of two parts:
1. The pattern to search for: `/<[^>]*>/`
    - This pattern searches for any tag in the string.
2. The replacement string: `''`
    - This is an empty string which will replace any tag found in the string.

## Helpful links
- [PHP preg_replace() Function](https://www.w3schools.com/php/func_preg_replace.asp)

onelinerhub: [How to remove a tag from a string using PHP regex?](https://onelinerhub.com/php-regex/how-to-remove-a-tag-from-a-string-using-php-regex)