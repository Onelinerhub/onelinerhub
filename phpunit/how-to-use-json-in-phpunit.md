# How to use JSON in PHPUnit?
// plain

JSON can be used in PHPUnit to test the output of a function or method.

## Example code

```
<?php

class MyTest extends \PHPUnit\Framework\TestCase
{
    public function testJson()
    {
        $data = array('name' => 'John', 'age' => 30);
        $json = json_encode($data);
        $this->assertJson($json);
    }
}
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation

- `$data`: An array containing data to be encoded into JSON
- `json_encode($data)`: Encodes the data into JSON
- `$this->assertJson($json)`: Asserts that the given string is valid JSON

## Helpful links
- [PHPUnit Documentation - Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertjson)

onelinerhub: [How to use JSON in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-json-in-phpunit)