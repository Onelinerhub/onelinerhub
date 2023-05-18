# How to match a GUID using regex in PHP?
// plain

A GUID (Globally Unique Identifier) is a 128-bit number used to identify resources in a unique way. To match a GUID using regex in PHP, you can use the following code:

```
$regex = '/^\{?[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}\}?$/';

if (preg_match($regex, $guid)) {
    echo "Matched!";
}
```

The code above uses the following parts:

- `$regex`: The regex pattern used to match the GUID. It consists of 8 hexadecimal characters, followed by a hyphen, followed by 3 groups of 4 hexadecimal characters, followed by a hyphen, followed by 12 hexadecimal characters.
- `preg_match()`: The PHP function used to match the regex pattern against the given string. It takes two parameters: the regex pattern and the string to match against.
- `$guid`: The string to match against.

If the string matches the regex pattern, the `preg_match()` function will return `true` and the output will be `Matched!`.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expression to Match a GUID](https://stackoverflow.com/questions/136505/regular-expression-to-match-a-guid)

onelinerhub: [How to match a GUID using regex in PHP?](https://onelinerhub.com/php-regex/how-to-match-a-guid-using-regex-in-php)