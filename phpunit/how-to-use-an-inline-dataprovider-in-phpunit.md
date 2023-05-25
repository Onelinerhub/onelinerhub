# How to use an inline dataprovider in PHPUnit?
// plain

Inline dataproviders are used to provide data to a test method in PHPUnit. It is a simple way to pass multiple sets of data to a test method.

## Example code

```
public function provider()
{
    return [
        [1, 2, 3],
        [4, 5, 9],
        [7, 8, 15]
    ];
}

/**
 * @dataProvider provider
 */
public function testAdd($a, $b, $expected)
{
    $this->assertEquals($expected, $a + $b);
}
```

## Output example

```
OK (3 tests, 3 assertions)
```

## Code explanation

- `public function provider()`: This is the function that returns the data to be used in the test method.
- `@dataProvider provider`: This is the annotation that tells PHPUnit which function to use as the data provider.
- `$this->assertEquals($expected, $a + $b)`: This is the assertion that is used to check the result of the test.

## Helpful links
- [PHPUnit Documentation - Data Providers](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#data-providers)

onelinerhub: [How to use an inline dataprovider in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-an-inline-dataprovider-in-phpunit)