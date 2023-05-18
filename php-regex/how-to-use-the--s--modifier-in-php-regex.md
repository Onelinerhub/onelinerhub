# How to use the "s" modifier in PHP regex?
// plain

The "s" modifier in PHP regex is used to make the dot (.) character match all characters, including newline characters. This allows the regex to match across multiple lines.

## Example code

```
$string = "This is a
multiline string";

$pattern = "/This.*string/s";

if (preg_match($pattern, $string)) {
    echo "Match found!";
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string`: This is the string that the regex will be applied to.
- `$pattern`: This is the regex pattern that will be used to match against the string. The `s` modifier is used to make the dot (.) character match all characters, including newline characters.
- `preg_match()`: This is the PHP function used to apply the regex pattern to the string.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expression Syntax](https://www.php.net/manual/en/regexp.reference.syntax.php)

onelinerhub: [How to use the "s" modifier in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-the--s--modifier-in-php-regex)