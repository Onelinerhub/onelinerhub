# How to generate a coverage report with PHPUnit?
// plain

PHPUnit provides a way to generate a coverage report to measure the amount of code covered by tests. To generate a coverage report, the `--coverage-html` option must be used when running the tests.

```
phpunit --coverage-html ./report
```

This will generate a coverage report in the `./report` directory. The report will contain information about the lines of code executed, classes, methods, and functions.

## Code explanation


- `--coverage-html`: This option is used to generate a coverage report.
- `./report`: This is the directory where the report will be generated.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/index.html)
- [PHPUnit Coverage Reports](https://phpunit.readthedocs.io/en/9.2/logging.html#coverage-reports)

onelinerhub: [How to generate a coverage report with PHPUnit?](https://onelinerhub.com/phpunit/how-to-generate-a-coverage-report-with-phpunit)