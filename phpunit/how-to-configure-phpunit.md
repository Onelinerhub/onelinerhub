# How to configure PHPUnit?
// plain

PHPUnit is a unit testing framework for the PHP programming language. It can be configured in several ways:

1. **Configuration File**: A configuration file can be used to set up the environment for PHPUnit. The configuration file should be named `phpunit.xml` and placed in the root directory of the project. The following example shows a basic configuration file:

```xml
<phpunit>
    <testsuites>
        <testsuite name="My Test Suite">
            <directory>./tests/</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

2. **Command Line Options**: PHPUnit can also be configured using command line options. For example, the following command will run all tests in the `tests` directory:

```
phpunit --bootstrap ./tests/bootstrap.php ./tests
```

3. **Environment Variables**: PHPUnit can also be configured using environment variables. For example, the following environment variable will set the default bootstrap file:

```
PHPUNIT_BOOTSTRAP=./tests/bootstrap.php
```

For more information, please refer to the [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [How to configure PHPUnit?](https://onelinerhub.com/phpunit/how-to-configure-phpunit)