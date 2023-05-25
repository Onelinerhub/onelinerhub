# How to test private methods in PHPUnit?
// plain

Private methods can be tested in PHPUnit by using the `ReflectionMethod` class. This class allows access to private methods and properties of a class.

```php
class MyClass
{
    private function privateMethod()
    {
        return 'privateMethod';
    }
}

$reflection = new ReflectionMethod('MyClass', 'privateMethod');
$reflection->setAccessible(true);
echo $reflection->invoke(new MyClass());
```

## Output example

```
privateMethod
```

1. Create a new instance of the `ReflectionMethod` class, passing in the class name and method name as parameters.
2. Set the `setAccessible` method to `true` to allow access to the private method.
3. Invoke the method using the `invoke` method, passing in an instance of the class.

## Helpful links

- [PHP Documentation - ReflectionMethod](https://www.php.net/manual/en/class.reflectionmethod.php)
- [PHPUnit Documentation - Testing Private Methods](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#testing-private-methods)

onelinerhub: [How to test private methods in PHPUnit?](https://onelinerhub.com/phpunit/how-to-test-private-methods-in-phpunit)