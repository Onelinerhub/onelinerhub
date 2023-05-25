# How to use PHPUnit json assert?
// plain

PHPUnit json assert is a method used to compare two JSON strings. It can be used to check if two JSON strings are equal or not.

## Example code

```
$json1 = '{"name":"John","age":30,"city":"New York"}';
$json2 = '{"name":"John","age":30,"city":"New York"}';
$this->assertJsonStringEqualsJsonString($json1, $json2);
```

## Output example

```
OK
```

## Code explanation

- `$json1` and `$json2`: two JSON strings to be compared
- `assertJsonStringEqualsJsonString()`: the method used to compare two JSON strings

## Helpful links
- [PHPUnit Documentation - Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertjsonstringequalsjsonstring)

onelinerhub: [How to use PHPUnit json assert?](https://onelinerhub.com/phpunit/how-to-use-phpunit-json-assert)