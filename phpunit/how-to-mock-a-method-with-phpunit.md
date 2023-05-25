# How to mock a method with PHPUnit?
// plain

PHPUnit provides a `mock` method to create a mock object of a class or interface. This mock object can be used to replace the actual class or interface in unit tests.

## Example code

```
$mock = $this->getMockBuilder('MyClass')
             ->setMethods(array('myMethod'))
             ->getMock();
```

This code creates a mock object of the `MyClass` class with the `myMethod` method mocked.

## Code explanation

- `$this->getMockBuilder('MyClass')`: creates a mock object of the `MyClass` class.
- `->setMethods(array('myMethod'))`: specifies the methods to be mocked.
- `->getMock()`: returns the mock object.

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#test-doubles)

onelinerhub: [How to mock a method with PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-method-with-phpunit)