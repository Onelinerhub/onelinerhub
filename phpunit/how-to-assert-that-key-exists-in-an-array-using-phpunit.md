# How to assert that key exists in an array using PHPUnit?
// plain

Asserting that a key exists in an array using PHPUnit can be done using the `assertArrayHasKey()` method. This method takes two parameters, the first being the array to check and the second being the key to check for.

```
$array = array('key1' => 'value1', 'key2' => 'value2');
$this->assertArrayHasKey('key1', $array);
```

The output of the above code will be a success if the key exists in the array, and a failure if it does not.

## Code explanation


1. `assertArrayHasKey()` - The method used to assert that a key exists in an array.
2. `$array` - The array to check for the key.
3. `'key1'` - The key to check for in the array.
4. `$this` - The object used to call the method.

## Helpful links

- [PHPUnit Documentation - assertArrayHasKey](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertarrayhaskey)

onelinerhub: [How to assert that key exists in an array using PHPUnit?](https://onelinerhub.com/phpunit/how-to-assert-that-key-exists-in-an-array-using-phpunit)