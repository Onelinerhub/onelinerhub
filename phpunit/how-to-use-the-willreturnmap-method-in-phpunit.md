# How to use the willReturnMap method in PHPUnit?
// plain

The `willReturnMap` method in PHPUnit is used to specify a map of arguments to return values when a specific method is called. This is useful for testing methods that take multiple arguments and return different values based on the arguments.

## Example

```
$mock = $this->getMockBuilder(MyClass::class)
    ->setMethods(['myMethod'])
    ->getMock();

$mock->expects($this->any())
    ->method('myMethod')
    ->willReturnMap([
        [1, 2, 3, 'foo'],
        [4, 5, 6, 'bar'],
    ]);

$this->assertEquals('foo', $mock->myMethod(1, 2, 3));
$this->assertEquals('bar', $mock->myMethod(4, 5, 6));
```
## Output example

```
foo
bar
```

## Code explanation


1. `$mock = $this->getMockBuilder(MyClass::class)`: This creates a mock object of the class `MyClass`.
2. `->setMethods(['myMethod'])`: This sets the methods to be mocked. In this case, only the method `myMethod` is mocked.
3. `->willReturnMap([[1, 2, 3, 'foo'], [4, 5, 6, 'bar']])`: This specifies a map of arguments to return values when `myMethod` is called. In this example, when `myMethod` is called with arguments `1, 2, 3`, it will return `foo`, and when it is called with arguments `4, 5, 6`, it will return `bar`.
4. `$this->assertEquals('foo', $mock->myMethod(1, 2, 3))`: This asserts that the return value of `myMethod` when called with arguments `1, 2, 3` is `foo`.
5. `$this->assertEquals('bar', $mock->myMethod(4, 5, 6))`: This asserts that the return value of `myMethod` when called with arguments `4, 5, 6` is `bar`.

## Helpful links

- [PHPUnit Documentation - willReturnMap](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#willreturnmap)