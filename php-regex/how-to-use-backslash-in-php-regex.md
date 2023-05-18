# How to use backslash in PHP regex?
// plain

Using backslash in PHP regex is a way to escape special characters. For example, if you want to match a literal dot character, you need to escape it with a backslash.

```
$string = 'This is a string with a dot.';
$pattern = '/\./';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string = 'This is a string with a dot.';` - This is the string we are searching in.
- `$pattern = '/\./';` - This is the pattern we are searching for. The backslash is used to escape the dot character, so that it is treated as a literal character instead of a special character.
- `if (preg_match($pattern, $string)) {` - This is the function that is used to search for the pattern in the string.
- `echo 'Match found!';` - This is the output that is printed if a match is found.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use backslash in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-backslash-in-php-regex)