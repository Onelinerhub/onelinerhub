# How to use PHPUnit assert to check an array?
// plain

PHPUnit assert is a powerful tool for testing the correctness of your code. It can be used to check an array by using the `assertEquals()` method.

```
$expected = array('a', 'b', 'c');
$actual = array('a', 'b', 'c');

$this->assertEquals($expected, $actual);
```

The above code will check if the two arrays are equal. If they are, the test will pass.

## Code explanation


- `$expected`: The expected array.
- `$actual`: The actual array.
- `assertEquals()`: The method used to compare the two arrays.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/)
- [PHPUnit Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html)

onelinerhub: [How to use PHPUnit assert to check an array?](https://onelinerhub.com/phpunit/how-to-use-phpunit-assert-to-check-an-array)