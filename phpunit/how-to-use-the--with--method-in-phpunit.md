# How to use the 'with' method in PHPUnit?
// plain

The `with` method in PHPUnit is used to pass parameters to a test method. It is used to set up the environment for the test.

## Example

```
public function testSomething()
{
    $this->with(['foo' => 'bar'])
         ->assertEquals('bar', $this->getFoo());
}
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation

- `with`: This is the method used to pass parameters to a test method.
- `['foo' => 'bar']`: This is the parameter being passed to the test method.
- `assertEquals`: This is the assertion method used to check if the expected result is equal to the actual result.
- `getFoo()`: This is the method used to get the value of the parameter passed to the test method.

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/)