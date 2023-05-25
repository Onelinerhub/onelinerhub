# How to enable verbose mode in PHPUnit?
// plain

Verbose mode in PHPUnit can be enabled by using the `--verbose` flag when running the test suite.

## Example

```
phpunit --verbose
```

## Output example

```
PHPUnit 8.5.2 by Sebastian Bergmann and contributors.

Runtime:       PHP 7.4.3
Configuration: /path/to/phpunit.xml

............................................................  63 / 63 (100%)

Time: 00:00.073, Memory: 6.00 MB

OK (63 tests, 63 assertions)
```

The `--verbose` flag will output more information about the tests being run, such as the number of tests and assertions, the time taken to run the tests, and the memory used.

The `--verbose` flag can also be combined with other flags, such as `--testdox` to output the tests in a more readable format.

## Example

```
phpunit --verbose --testdox
```

## Output example

```
PHPUnit 8.5.2 by Sebastian Bergmann and contributors.

Runtime:       PHP 7.4.3
Configuration: /path/to/phpunit.xml

MyTestClass
 [x] My first test
 [x] My second test

Time: 00:00.073, Memory: 6.00 MB

OK (2 tests, 2 assertions)
```

## Helpful links
- [PHPUnit Documentation - Command Line Options](https://phpunit.readthedocs.io/en/9.2/textui.html#command-line-options)