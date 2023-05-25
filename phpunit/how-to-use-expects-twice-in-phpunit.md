# How to use expects twice in PHPUnit?
// plain

Using `expects` twice in PHPUnit is possible by using the `expectException` and `expectExceptionMessage` methods.

## Example code

```
public function testException()
{
    $this->expectException(Exception::class);
    $this->expectExceptionMessage('Exception message');
    throw new Exception('Exception message');
}
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation

- `$this->expectException(Exception::class);` - This line sets the expectation that an exception of type `Exception` will be thrown.
- `$this->expectExceptionMessage('Exception message');` - This line sets the expectation that the exception thrown will have the message `Exception message`.
- `throw new Exception('Exception message');` - This line throws an exception of type `Exception` with the message `Exception message`.

## Helpful links
- [PHPUnit Documentation - expectException](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#testing-exceptions)
- [PHPUnit Documentation - expectExceptionMessage](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#testing-exceptions)

onelinerhub: [How to use expects twice in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-expects-twice-in-phpunit)