# How to stop PHPUnit on failure?
// plain

You can stop PHPUnit on failure by using the `stopOnFailure` option. This option will cause PHPUnit to stop execution after the first failure.

## Example code

```
$ phpunit --stop-on-failure
```

## Output example

```
PHPUnit 6.5.14 by Sebastian Bergmann and contributors.

.F

Time: 1.02 seconds, Memory: 10.00MB

There was 1 failure:

1) Tests\ExampleTest::testTrue
Failed asserting that false is true.

/path/to/ExampleTest.php:14

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

The `stopOnFailure` option is a boolean option, which means it can be set to either `true` or `false`. When set to `true`, PHPUnit will stop execution after the first failure. When set to `false`, PHPUnit will continue execution even after a failure.

## Code explanation

- `--stop-on-failure`: This is the option that will cause PHPUnit to stop execution after the first failure.
- `true`: When set to `true`, PHPUnit will stop execution after the first failure.
- `false`: When set to `false`, PHPUnit will continue execution even after a failure.

## Helpful links
- [PHPUnit Documentation - Stop On Failure](https://phpunit.readthedocs.io/en/latest/textui.html#stop-on-failure)

onelinerhub: [How to stop PHPUnit on failure?](https://onelinerhub.com/phpunit/how-to-stop-phpunit-on-failure)