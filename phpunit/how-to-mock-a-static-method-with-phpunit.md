# How to mock a static method with PHPUnit?
// plain

Mocking static methods with PHPUnit is possible using the `getMockForAbstractClass` method.

```
class MyClass
{
    public static function myStaticMethod()
    {
        return 'foo';
    }
}

$mock = $this->getMockForAbstractClass('MyClass');
$mock->expects($this->any())
     ->method('myStaticMethod')
     ->will($this->returnValue('bar'));

echo MyClass::myStaticMethod();
```

## Output example

```
bar
```

The code above creates a mock object of the `MyClass` class and overrides the `myStaticMethod` method to return `bar` instead of `foo`.

## Code explanation

- `getMockForAbstractClass`: creates a mock object of the specified class
- `expects`: specifies the expectation of the mock object
- `method`: specifies the method to be overridden
- `will`: specifies the return value of the overridden method

## Helpful links
- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)

onelinerhub: [How to mock a static method with PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-static-method-with-phpunit)