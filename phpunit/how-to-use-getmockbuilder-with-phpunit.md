# How to use getMockBuilder with PHPUnit?
// plain

Using `getMockBuilder` with PHPUnit allows you to create a mock object of a class or interface. This mock object can be used to test the behavior of a class or interface without having to create a real instance of it.

## Example

```
$mock = $this->getMockBuilder(MyClass::class)
    ->setMethods(['myMethod'])
    ->getMock();
```

This example creates a mock object of the `MyClass` class with the `myMethod` method mocked.

## Code explanation

- `$this->getMockBuilder(MyClass::class)`: creates a mock object of the `MyClass` class.
- `->setMethods(['myMethod'])`: mocks the `myMethod` method.
- `->getMock()`: returns the mock object.

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)

onelinerhub: [How to use getMockBuilder with PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-getmockbuilder-with-phpunit)