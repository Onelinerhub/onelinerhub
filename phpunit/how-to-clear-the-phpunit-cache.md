# How to clear the PHPUnit cache?
// plain

The PHPUnit cache can be cleared by using the `--clear-cache` option when running the `phpunit` command.

For example:
```
phpunit --clear-cache
```

This will clear the cache and the output should look like this:
```
Clearing cache...

OK
```

The `--clear-cache` option can also be used with other options such as `--configuration` or `--bootstrap` to clear the cache for a specific configuration or bootstrap file.

For more information, please refer to the [PHPUnit documentation](https://phpunit.readthedocs.io/en/9.2/textui.html#command-line-options).

onelinerhub: [How to clear the PHPUnit cache?](https://onelinerhub.com/phpunit/how-to-clear-the-phpunit-cache)