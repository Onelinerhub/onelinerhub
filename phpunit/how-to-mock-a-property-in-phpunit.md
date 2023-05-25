# How to mock a property in PHPUnit?
// plain

Mocking a property in PHPUnit can be done using the `setProperty` method of the `PHPUnit_Framework_TestCase` class.

```
$mock = $this->getMockBuilder('MyClass')
             ->setMethods(array('myMethod'))
             ->getMock();

$mock->expects($this->any())
     ->method('myMethod')
     ->will($this->returnValue('foo'));

$this->setProperty($mock, 'myProperty', 'bar');
```

The code above will set the `myProperty` property of the `MyClass` mock object to `bar`.

## Code explanation


1. `$mock = $this->getMockBuilder('MyClass')` - creates a mock object of the `MyClass` class.
2. `->setMethods(array('myMethod'))` - sets the methods to be mocked.
3. `->getMock();` - returns the mock object.
4. `$mock->expects($this->any())` - sets the expectation for the `myMethod` method.
5. `->method('myMethod')` - specifies the method to be mocked.
6. `->will($this->returnValue('foo'));` - sets the return value for the `myMethod` method.
7. `$this->setProperty($mock, 'myProperty', 'bar');` - sets the `myProperty` property of the `MyClass` mock object to `bar`.

## Output example


No output.

## Helpful links

- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)
- [PHPUnit Documentation - setProperty](https://phpunit.readthedocs.io/en/9.2/api/PHPUnit_Framework_TestCase.html#method_setProperty)

onelinerhub: [How to mock a property in PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-property-in-phpunit)