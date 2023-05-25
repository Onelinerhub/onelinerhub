# How to use dependency injection in PHPUnit?
// plain

Dependency injection is a technique used to inject dependencies into a class. It can be used in PHPUnit to inject dependencies into a test class. This allows for better test isolation and makes the tests more maintainable.

## Example code

```
class MyTest extends \PHPUnit\Framework\TestCase
{
    private $dependency;

    public function __construct($dependency)
    {
        $this->dependency = $dependency;
    }

    public function testSomething()
    {
        // Test something with $this->dependency
    }
}
```

The code above shows an example of how to use dependency injection in PHPUnit. The test class is extended from the PHPUnit TestCase class and a dependency is injected into the constructor. The dependency can then be used in the test method.

## Code explanation

- `class MyTest extends \PHPUnit\Framework\TestCase`: This line extends the test class from the PHPUnit TestCase class.
- `public function __construct($dependency)`: This is the constructor of the test class. It takes a dependency as an argument.
- `$this->dependency = $dependency`: This line assigns the dependency to a class property.
- `public function testSomething()`: This is the test method. It can use the dependency to test something.

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [Dependency Injection in PHPUnit](https://www.sitepoint.com/dependency-injection-in-phpunit/)

onelinerhub: [How to use dependency injection in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-dependency-injection-in-phpunit)