# How to use PHP regex to match a hashtag?
// plain

Using PHP regex to match a hashtag is a simple process. The following example code block will match a hashtag in a string:

```
$string = 'This is a #hashtag';
preg_match('/#([a-zA-Z0-9_]+)/', $string, $matches);
```

The output of the example code will be:

```
Array
(
    [0] => #hashtag
    [1] => hashtag
)
```

## Code explanation


- `$string = 'This is a #hashtag';`: This is the string that contains the hashtag.

- `preg_match('/#([a-zA-Z0-9_]+)/', $string, $matches);`: This is the regular expression used to match the hashtag. The `#` symbol is used to match the hashtag, and the `([a-zA-Z0-9_]+)` part is used to match the characters in the hashtag.

- `$matches`: This is the array that will contain the matches from the regular expression.

## Helpful links

- [PHP Regular Expression Functions](https://www.w3schools.com/php/php_regex.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a hashtag?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-hashtag)