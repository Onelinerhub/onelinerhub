# How to use PHP regex to match UUID?
// plain

A UUID (Universally Unique Identifier) is a 128-bit number used to identify information in computer systems. To match a UUID with a regular expression in PHP, you can use the following code:

```
$uuid = '123e4567-e89b-12d3-a456-426655440000';

if (preg_match('/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/', $uuid)) {
    echo 'Valid UUID';
} else {
    echo 'Invalid UUID';
}
```

## Output example

```
Valid UUID
```

The code consists of the following parts:

1. `$uuid = '123e4567-e89b-12d3-a456-426655440000';` - This is the UUID that we are trying to match.

2. `preg_match('/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/', $uuid)` - This is the regular expression used to match the UUID. It consists of five parts, each of which is enclosed in square brackets and followed by a number in curly braces. The first part matches any 8 hexadecimal digits, the second part matches any 4 hexadecimal digits, the third part matches any 4 hexadecimal digits, the fourth part matches any 4 hexadecimal digits, and the fifth part matches any 12 hexadecimal digits.

3. `if (preg_match('/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/', $uuid)) {` - This is the if statement that checks if the regular expression matches the UUID.

4. `echo 'Valid UUID';` - This is the code that is executed if the regular expression matches the UUID.

5. `echo 'Invalid UUID';` - This is the code that is executed if the regular expression does not match the UUID.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match UUID?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-uuid)