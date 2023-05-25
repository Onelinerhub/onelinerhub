# How to use filters with PHPUnit?
// plain

Filters can be used with PHPUnit to limit the tests that are run. This is useful when you want to focus on a specific set of tests.

## Example

```
$ phpunit --filter testName
```

This will run only the tests that match the given name.

## Code explanation


1. `phpunit` - This is the command used to run the tests.
2. `--filter` - This is the flag used to specify the filter.
3. `testName` - This is the name of the test to be run.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/index.html)

onelinerhub: [How to use filters with PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-filters-with-phpunit)