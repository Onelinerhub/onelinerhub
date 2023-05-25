# How to write a feature test with PHPUnit?
// plain

Feature tests are used to test the functionality of a feature in an application. PHPUnit is a popular testing framework for PHP applications.

To write a feature test with PHPUnit, you need to create a test class that extends the PHPUnit_Framework_TestCase class. Then, you need to create a test method that contains the code to test the feature.

## Example code

```
class FeatureTest extends PHPUnit_Framework_TestCase
{
    public function testFeature()
    {
        // code to test the feature
    }
}
```

## Output example

```
OK (1 test, 0 assertions)
```

## Code explanation

- `class FeatureTest extends PHPUnit_Framework_TestCase` - This line creates a test class that extends the PHPUnit_Framework_TestCase class.
- `public function testFeature()` - This line creates a test method that contains the code to test the feature.
- `// code to test the feature` - This line contains the code to test the feature.

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [Writing Tests with PHPUnit](https://phpunit.readthedocs.io/en/latest/writing-tests-for-phpunit.html)

onelinerhub: [How to write a feature test with PHPUnit?](https://onelinerhub.com/phpunit/how-to-write-a-feature-test-with-phpunit)