# How to mock a method with different arguments in PHPUnit?
// plain

PHPUnit provides a powerful mocking framework that allows us to mock methods with different arguments. We can use the `expects()` method to specify the arguments that the mocked method should expect. For example:

```
$mock = $this->getMockBuilder('MyClass')
             ->setMethods(['myMethod'])
             ->getMock();

$mock->expects($this->once())
     ->method('myMethod')
     ->with($this->equalTo('arg1'), $this->equalTo('arg2'));
```

This will ensure that the `myMethod` method is called with the arguments `arg1` and `arg2`.

## Code explanation


1. `$mock = $this->getMockBuilder('MyClass')
             ->setMethods(['myMethod'])
             ->getMock();` - This creates a mock object of the class `MyClass` and sets the `myMethod` method as the only method to be mocked.

2. `$mock->expects($this->once())
     ->method('myMethod')
     ->with($this->equalTo('arg1'), $this->equalTo('arg2'));` - This specifies that the `myMethod` method should be called with the arguments `arg1` and `arg2`.

## Helpful links

- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)

onelinerhub: [How to mock a method with different arguments in PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-method-with-different-arguments-in-phpunit)