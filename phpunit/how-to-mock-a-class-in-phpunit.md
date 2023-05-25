# How to mock a class in PHPUnit?
// plain

Mocking a class in PHPUnit is a way to test a class in isolation from other classes. It allows us to replace the real class with a dummy class that can be used to simulate the behavior of the real class.

## Example code

```
$mock = $this->getMockBuilder('MyClass')
             ->setMethods(array('myMethod'))
             ->getMock();
```

## Code explanation

- `$this->getMockBuilder('MyClass')`: This creates a mock object of the class `MyClass`.
- `->setMethods(array('myMethod'))`: This sets the methods that should be mocked.
- `->getMock()`: This returns the mock object.

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)

onelinerhub: [How to mock a class in PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-class-in-phpunit)