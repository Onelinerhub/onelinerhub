# How to use the PHPUnit command line interface (CLI)?
// plain

The PHPUnit command line interface (CLI) is a tool used to run tests written in PHPUnit. It can be used to run tests from the command line, and can be used to automate the running of tests.

To use the PHPUnit CLI, you must first install PHPUnit. This can be done using Composer, or by downloading the PHAR file.

Once PHPUnit is installed, you can run tests from the command line using the `phpunit` command. For example, to run a test file called `MyTest.php` in the current directory, you can use the following command:

```
phpunit MyTest.php
```

The output of this command will show the results of the tests, including any errors or failures.

You can also use the `--bootstrap` option to specify a bootstrap file, which will be run before the tests. This can be used to set up the environment for the tests. For example:

```
phpunit --bootstrap bootstrap.php MyTest.php
```

You can also use the `--configuration` option to specify a configuration file, which will be used to configure the tests.

For more information on using the PHPUnit CLI, see the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [How to use the PHPUnit command line interface (CLI)?](https://onelinerhub.com/phpunit/how-to-use-the-phpunit-command-line-interface--cli-)