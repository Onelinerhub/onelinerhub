# How to use PHPUnit annotations?
// plain

PHPUnit annotations are used to provide additional information about the tests. They are written in the docblock of the test method and start with an `@` symbol.

## Example

```
/**
 * @coversDefaultClass MyClass
 * @covers ::myMethod
 */
public function testMyMethod()
{
    // Test code
}
```

The example above will tell PHPUnit to test the `MyClass` class and the `myMethod` method.

The following annotations are available:

- `@covers`: Tells PHPUnit to test the specified class or method.
- `@depends`: Tells PHPUnit to run the specified test before running the current test.
- `@dataProvider`: Tells PHPUnit to use the specified data provider for the test.
- `@expectedException`: Tells PHPUnit to expect the specified exception to be thrown.
- `@group`: Tells PHPUnit to group the test with the specified group.

## Helpful links

- [PHPUnit Annotations](https://phpunit.readthedocs.io/en/latest/annotations.html)
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)

onelinerhub: [How to use PHPUnit annotations?](https://onelinerhub.com/phpunit/how-to-use-phpunit-annotations)