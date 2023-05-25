# How to create a mock object in PHPUnit?
// plain

Mock objects are used in unit testing to replace real objects. PHPUnit provides a framework for creating mock objects using the `getMock()` method.

## Example code

```
$mock = $this->getMock('MyClass', array('methodName'));
```

This code creates a mock object of the class `MyClass` and allows the `methodName` to be called.

## Code explanation

- `getMock()`: This is the method used to create a mock object.
- `MyClass`: This is the class that the mock object is based on.
- `methodName`: This is the name of the method that can be called on the mock object.

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#test-doubles)

onelinerhub: [How to create a mock object in PHPUnit?](https://onelinerhub.com/phpunit/how-to-create-a-mock-object-in-phpunit)