# How to install PHPUnit with Composer?
// plain

1. Install [Composer](https://getcomposer.org/download/) on your system.
2. Create a `composer.json` file in the root of your project and add the following code:
```json
{
    "require-dev": {
        "phpunit/phpunit": "^7.5"
    }
}
```
3. Run `composer install` in the root of your project.
4. Add the `vendor/bin` directory to your `PATH` environment variable.
5. Run `phpunit --version` to verify the installation.

## Output example

```
PHPUnit 7.5.20 by Sebastian Bergmann and contributors.
```

onelinerhub: [How to install PHPUnit with Composer?](https://onelinerhub.com/phpunit/how-to-install-phpunit-with-composer)