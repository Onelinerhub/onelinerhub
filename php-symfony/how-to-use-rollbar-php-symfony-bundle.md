# How to use Rollbar PHP Symfony Bundle?
// plain

Rollbar PHP Symfony Bundle is a library that allows you to easily integrate Rollbar error monitoring into your Symfony application. It provides a simple way to report errors and exceptions to Rollbar.

## Example code

```
use Rollbar\Rollbar;

$config = array(
    'access_token' => 'POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment' => 'production'
);
Rollbar::init($config);
```

This code initializes the Rollbar library with the given configuration. The `access_token` is the token for the project in Rollbar, and the `environment` is the environment of the application (e.g. production, staging, etc).

The bundle also provides a way to report errors and exceptions to Rollbar. For example, you can use the `RollbarNotifier` service to report an exception:

```
$rollbarNotifier = $this->get('rollbar.notifier');
$rollbarNotifier->reportException($exception);
```

This code will report the given exception to Rollbar.

## Helpful links

- [Rollbar PHP Symfony Bundle](https://github.com/rollbar/rollbar-php-symfony-bundle)
- [Rollbar Documentation](https://docs.rollbar.com/docs/php)

onelinerhub: [How to use Rollbar PHP Symfony Bundle?](https://onelinerhub.com/php-symfony/how-to-use-rollbar-php-symfony-bundle)