# How to mock a private method with PHPUnit?
// plain

Mocking private methods with PHPUnit is possible using the `getMockBuilder` method.

```
$mock = $this->getMockBuilder(MyClass::class)
    ->setMethods(['myPrivateMethod'])
    ->getMock();

$mock->expects($this->once())
    ->method('myPrivateMethod')
    ->willReturn('mocked result');
```

The code above will create a mock object of `MyClass` and set the `myPrivateMethod` to be mocked. The `expects` method will set the expectation that the `myPrivateMethod` will be called once and will return `mocked result`.

- `getMockBuilder`: creates a mock object of the given class
- `setMethods`: sets the methods to be mocked
- `expects`: sets the expectation that the method will be called
- `willReturn`: sets the return value of the mocked method

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#test-doubles)
- [PHPUnit Documentation - Mock Builder](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#test-doubles-mock-builder)

onelinerhub: [How to mock a private method with PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-private-method-with-phpunit)