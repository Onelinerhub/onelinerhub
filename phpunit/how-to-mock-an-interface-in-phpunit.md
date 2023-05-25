# How to mock an interface in PHPUnit?
// plain

Mocking an interface in PHPUnit can be done using the `getMockForAbstractClass()` method. This method takes the name of the interface as the first argument and an array of constructor arguments as the second argument.

```
$mock = $this->getMockForAbstractClass('MyInterface', array('arg1', 'arg2'));
```

The `getMockForAbstractClass()` method will create a mock object that implements the interface and can be used to test code that depends on the interface.

- `getMockForAbstractClass()`: This method takes the name of the interface as the first argument and an array of constructor arguments as the second argument.
- `MyInterface`: This is the name of the interface that is being mocked.
- `array('arg1', 'arg2')`: This is an array of constructor arguments that will be passed to the mock object.

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)

onelinerhub: [How to mock an interface in PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-an-interface-in-phpunit)