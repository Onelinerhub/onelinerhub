# How to generate a JUnit report in PHPUnit?
// plain

JUnit reports can be generated in PHPUnit by using the `--log-junit` option. This option will generate an XML file containing the test results.

## Example

```
phpunit --log-junit test-results.xml
```

The output of the above command will be an XML file containing the test results.

## Code explanation


1. `phpunit`: This is the command used to run the tests.
2. `--log-junit`: This is the option used to generate the JUnit report.
3. `test-results.xml`: This is the name of the XML file that will be generated containing the test results.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [JUnit XML Format](https://llg.cubic.org/docs/junit/)

onelinerhub: [How to generate a JUnit report in PHPUnit?](https://onelinerhub.com/phpunit/how-to-generate-a-junit-report-in-phpunit)