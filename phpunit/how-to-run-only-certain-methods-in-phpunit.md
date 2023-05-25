# How to run only certain methods in PHPUnit?
// plain

You can run only certain methods in PHPUnit by using the `--filter` option.

For example, to run only the `testAdd()` method in the `CalculatorTest` class, you can use the following command:

```
phpunit --filter testAdd CalculatorTest
```

This will run only the `testAdd()` method in the `CalculatorTest` class.

The parts of the command are:
- `phpunit`: the command to run PHPUnit
- `--filter`: the option to specify which method to run
- `testAdd`: the name of the method to run
- `CalculatorTest`: the name of the class containing the method

For more information, see the [PHPUnit documentation](https://phpunit.readthedocs.io/en/9.2/textui.html#running-tests-by-name).

onelinerhub: [How to run only certain methods in PHPUnit?](https://onelinerhub.com/phpunit/how-to-run-only-certain-methods-in-phpunit)