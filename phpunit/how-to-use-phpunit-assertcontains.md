# How to use PHPUnit assertcontains?
// plain

PHPUnit assertContains is a method used to check if a given value is contained in an array. It takes two parameters, the first being the expected value and the second being the array to search.

## Example code

```
$array = array('a', 'b', 'c');
$this->assertContains('b', $array);
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation

- `$array`: An array containing the values to search.
- `assertContains()`: The method used to check if a given value is contained in an array.
- `'b'`: The expected value to search for.

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertcontains)

onelinerhub: [How to use PHPUnit assertcontains?](https://onelinerhub.com/phpunit/how-to-use-phpunit-assertcontains)