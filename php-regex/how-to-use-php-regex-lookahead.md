# How to use PHP regex lookahead?
// plain

PHP regex lookahead is a powerful tool for pattern matching. It allows you to look ahead in a string and check for a certain pattern without actually consuming the characters.

## Example code

```
$string = 'Hello World';
$pattern = '/Hello(?=\sWorld)/';

if (preg_match($pattern, $string)) {
    echo 'Match found!';
}
```

## Output example

```
Match found!
```

## Code explanation

- `$string = 'Hello World';` - This is the string we are searching in.
- `$pattern = '/Hello(?=\sWorld)/';` - This is the pattern we are searching for. The `(?=\sWorld)` part is the lookahead assertion. It checks if the string contains `Hello` followed by a whitespace and `World`.
- `preg_match($pattern, $string)` - This function searches for the pattern in the string.
- `echo 'Match found!';` - This line is executed if the pattern is found.

## Helpful links
- [PHP Regex Lookahead](https://www.regular-expressions.info/lookaround.html)
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use PHP regex lookahead?](https://onelinerhub.com/php-regex/how-to-use-php-regex-lookahead)