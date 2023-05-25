# How to create a testsuite in PHPUnit?
// plain

Creating a testsuite in PHPUnit is a simple process.

```
<?php
class MyTestSuite extends PHPUnit_Framework_TestSuite
{
    public static function suite()
    {
        $suite = new PHPUnit_Framework_TestSuite('MyTestSuite');
        $suite->addTestSuite('MyTestCase1');
        $suite->addTestSuite('MyTestCase2');
        return $suite;
    }
}
?>
```

This example code creates a testsuite called `MyTestSuite` which contains two test cases `MyTestCase1` and `MyTestCase2`.

1. `class MyTestSuite extends PHPUnit_Framework_TestSuite` - This line creates a class called `MyTestSuite` which extends the `PHPUnit_Framework_TestSuite` class.
2. `public static function suite()` - This line creates a public static function called `suite` which will be used to create the testsuite.
3. `$suite = new PHPUnit_Framework_TestSuite('MyTestSuite');` - This line creates a new instance of the `PHPUnit_Framework_TestSuite` class and assigns it to the `$suite` variable.
4. `$suite->addTestSuite('MyTestCase1');` - This line adds the `MyTestCase1` test case to the `$suite` testsuite.
5. `$suite->addTestSuite('MyTestCase2');` - This line adds the `MyTestCase2` test case to the `$suite` testsuite.
6. `return $suite;` - This line returns the `$suite` testsuite.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [Creating Test Suites](https://phpunit.readthedocs.io/en/latest/organizing_tests.html#organizing-tests-into-test-suites)