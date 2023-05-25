# How to check if a JSON contains a value in PHPUnit?
// plain

To check if a JSON contains a value in PHPUnit, you can use the `assertJson()` method. This method takes two parameters, the first being the actual JSON string and the second being the expected JSON string.

## Example code

```
$actualJson = '{"name":"John","age":30}';
$expectedJson = '{"name":"John"}';

$this->assertJson($actualJson, $expectedJson);
```

## Output example

```
OK
```

The `assertJson()` method will compare the two JSON strings and check if the actual JSON string contains the expected JSON string. If the expected JSON string is found in the actual JSON string, the test will pass.

## Code explanation

- `assertJson()`: The method used to check if a JSON contains a value in PHPUnit.
- `$actualJson`: The actual JSON string to be tested.
- `$expectedJson`: The expected JSON string to be found in the actual JSON string.

## Helpful links
- [PHPUnit Documentation - assertJson](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertjson)

onelinerhub: [How to check if a JSON contains a value in PHPUnit?](https://onelinerhub.com/phpunit/how-to-check-if-a-json-contains-a-value-in-phpunit)