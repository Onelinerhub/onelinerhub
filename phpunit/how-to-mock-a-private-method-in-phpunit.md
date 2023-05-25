# How to mock a private method in PHPUnit?
// plain

Mocking private methods in PHPUnit is possible using the `getMockBuilder` method.

```
$mock = $this->getMockBuilder(MyClass::class)
    ->setMethods(['myPrivateMethod'])
    ->getMock();

$mock->expects($this->once())
    ->method('myPrivateMethod')
    ->willReturn('mocked result');
```

The above code will create a mock object of `MyClass` and override the `myPrivateMethod` method with a mocked result.

- `getMockBuilder`: creates a mock object of the specified class
- `setMethods`: overrides the specified methods with mocked results
- `expects`: specifies the expectation of the mocked method
- `method`: specifies the method to be mocked
- `willReturn`: specifies the return value of the mocked method

## Helpful links
- https://phpunit.readthedocs.io/en/9.2/test-doubles.html#test-doubles
- https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mocking-private-methods

onelinerhub: [How to mock a private method in PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-private-method-in-phpunit)