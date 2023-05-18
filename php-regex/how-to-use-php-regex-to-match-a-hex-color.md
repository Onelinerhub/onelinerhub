# How to use PHP regex to match a hex color?
// plain

To match a hex color with PHP regex, you can use the following code:

```
$hex_color = "#FFF";
if (preg_match('/^#[a-f0-9]{6}$/i', $hex_color)) {
    echo "Valid hex color";
} else {
    echo "Invalid hex color";
}
```

The output of this code will be:

```
Valid hex color
```

The code consists of the following parts:

- `$hex_color = "#FFF";` - this is the variable containing the hex color to be matched.
- `preg_match('/^#[a-f0-9]{6}$/i', $hex_color)` - this is the regular expression used to match the hex color. It matches a string that starts with a `#` followed by 6 characters from `a-f` or `0-9` and ends with the same character. The `i` flag at the end makes the expression case-insensitive.
- `echo "Valid hex color";` - this is the output when the hex color is valid.
- `echo "Invalid hex color";` - this is the output when the hex color is invalid.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a hex color?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-hex-color)