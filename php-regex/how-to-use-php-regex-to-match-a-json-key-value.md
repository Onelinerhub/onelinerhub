# How to use PHP regex to match a JSON key value?
// plain

Using PHP regex to match a JSON key value is a powerful way to parse and extract data from a JSON string. The following example code block shows how to use regex to match a JSON key value:
```
$json = '{"name":"John","age":30,"city":"New York"}';

preg_match('/\"name\":\"(.*?)\"/', $json, $name);
echo $name[1];
```
The output of the example code is:
```
John
```
## Code explanation


1. `$json = '{"name":"John","age":30,"city":"New York"}';` - This is the JSON string that we are trying to parse.

2. `preg_match('/\"name\":\"(.*?)\"/', $json, $name);` - This is the regex expression used to match the JSON key value. The `\"name\":\"` part of the expression matches the key, and the `(.*?)` part of the expression matches the value.

3. `echo $name[1];` - This line of code prints out the value of the matched key.

## Helpful links

- [PHP Regular Expressions](https://www.php.net/manual/en/book.pcre.php)
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)

onelinerhub: [How to use PHP regex to match a JSON key value?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-json-key-value)