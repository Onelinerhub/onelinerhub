# How to run tests in parallel with PHPUnit?
// plain

PHPUnit supports running tests in parallel using the `--process-isolation` option. This option will run each test in a separate process, allowing them to run in parallel.

```
phpunit --process-isolation
```

The output of the command will look something like this:

```
PHPUnit 8.5.2 by Sebastian Bergmann and contributors.

Runtime:       PHP 7.4.3
Configuration: /path/to/phpunit.xml

............................................................  63 / 63 (100%)

Time: 00:00.845, Memory: 10.00 MB

OK (63 tests, 63 assertions)
```

The `--process-isolation` option can also be used in combination with other options, such as `--testsuite` to run tests in a specific test suite in parallel.

```
phpunit --process-isolation --testsuite MyTestSuite
```

For more information, see the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/textui.html#running-tests-in-parallel).

onelinerhub: [How to run tests in parallel with PHPUnit?](https://onelinerhub.com/phpunit/how-to-run-tests-in-parallel-with-phpunit)