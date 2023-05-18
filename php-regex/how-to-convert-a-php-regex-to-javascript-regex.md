# How to convert a PHP regex to JavaScript regex?
// plain

To convert a PHP regex to JavaScript regex, you need to understand the differences between the two languages. The main difference is that JavaScript does not support the `\e` escape sequence, so you need to replace it with `\u001B`. Additionally, JavaScript does not support the `\Q` and `\E` sequences, so you need to use `(?:` and `)` instead.

## Example code

```
// PHP regex
$pattern = '/\QHello\E World/';

// JavaScript regex
let pattern = /(?:Hello) World/;
```

## Output example

```
// No output
```

## Code explanation

- `\Q` and `\E` sequences: These sequences are used to escape any special characters in the pattern. In JavaScript, you need to use `(?:` and `)` instead.
- `\e` escape sequence: This sequence is used to escape special characters in the pattern. In JavaScript, you need to replace it with `\u001B`.

## Helpful links
- [PHP Regex](https://www.php.net/manual/en/book.pcre.php)
- [JavaScript Regex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)

onelinerhub: [How to convert a PHP regex to JavaScript regex?](https://onelinerhub.com/php-regex/how-to-convert-a-php-regex-to-javascript-regex)