# How to use PHP regex to match a multiline?
// plain

Using PHP regex to match a multiline is possible with the `/m` modifier. This modifier allows the pattern to match across multiple lines.

## Example code

```
$string = "This is a
multiline string";

$pattern = "/This.*string/m";

if (preg_match($pattern, $string)) {
    echo "Match found!";
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string`: This is the string that will be searched for a match.
- `$pattern`: This is the regular expression pattern that will be used to search for a match.
- `preg_match()`: This is the PHP function used to search for a match. It takes two parameters, the regular expression pattern and the string to search.
- `/m`: This is the modifier used to allow the pattern to match across multiple lines.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [How to use PHP regex to match a multiline?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-multiline)