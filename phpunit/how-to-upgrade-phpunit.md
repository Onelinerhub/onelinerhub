# How to upgrade PHPUnit?
// plain

Upgrading PHPUnit is a simple process. To upgrade, you need to run the following command in your terminal:

```
composer update phpunit/phpunit
```

This will update the version of PHPUnit to the latest version available.

The command will output something like this:

```
Updating dependencies (including require-dev)
  - Updating phpunit/phpunit (7.5.20 => 8.5.8)
```

The command:

1. `composer update`: updates all dependencies in the `composer.json` file.
2. `phpunit/phpunit`: specifies the package to update.
3. `7.5.20 => 8.5.8`: shows the version of PHPUnit that is being updated.

For more information, please refer to the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/installation.html).