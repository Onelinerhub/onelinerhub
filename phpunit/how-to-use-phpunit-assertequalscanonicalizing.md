# How to use PHPUnit assertequalscanonicalizing?
// plain

PHPUnit's `assertEqualsCanonicalizing` is a method used to compare two values for equality, while ignoring differences in their order. It is useful for comparing arrays or objects that may have different orderings.

## Example

```
$expected = [1, 2, 3];
$actual = [3, 2, 1];

$this->assertEqualsCanonicalizing($expected, $actual);
```

## Output example

```
OK
```

## Code explanation

- `assertEqualsCanonicalizing`: The method used to compare two values for equality, while ignoring differences in their order.
- `$expected`: The expected value to compare against.
- `$actual`: The actual value to compare.

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertequalscanonicalizing)

onelinerhub: [How to use PHPUnit assertequalscanonicalizing?](https://onelinerhub.com/phpunit/how-to-use-phpunit-assertequalscanonicalizing)