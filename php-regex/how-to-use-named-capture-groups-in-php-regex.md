# How to use named capture groups in PHP regex?
// plain

Named capture groups are a powerful feature of regular expressions in PHP. They allow you to capture parts of a string and assign them to a variable. This makes it easier to work with the captured data.

## Example code

```
$string = 'This is a string';
preg_match('/This is (?<capture>\w+)/', $string, $matches);
echo $matches['capture'];
```

## Output example

```
a
```

## Code explanation

- `preg_match()`: This is a PHP function that takes a regular expression and a string as arguments and returns an array of matches.
- `(?<capture>\w+)`: This is the named capture group. It captures one or more word characters and assigns them to the variable `capture`.
- `$matches['capture']`: This is how you access the captured data.

## Helpful links
- [PHP preg_match()](https://www.php.net/manual/en/function.preg-match.php)
- [Regular Expressions](https://www.php.net/manual/en/book.pcre.php)

onelinerhub: [How to use named capture groups in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-named-capture-groups-in-php-regex)