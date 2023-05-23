# How to enable hot reload in PHP Symfony?
// plain

Hot reloading in PHP Symfony can be enabled by using the Symfony Web Server. This is a local web server that can be used to run Symfony applications. It supports hot reloading, which means that changes made to the code are automatically reflected in the browser without having to manually restart the server.

To enable hot reloading, first install the Symfony Web Server using the following command:

```
composer require server --dev
```

Then, start the server with the following command:

```
php bin/console server:start
```

The server will now be running and hot reloading will be enabled.

## Code explanation


1. `composer require server --dev`: This command installs the Symfony Web Server.
2. `php bin/console server:start`: This command starts the server and enables hot reloading.

## Helpful links

- [Symfony Web Server](https://symfony.com/doc/current/setup/symfony_server.html)
- [Hot Reloading](https://symfony.com/doc/current/setup/hot_reloading.html)

onelinerhub: [How to enable hot reload in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-enable-hot-reload-in-php-symfony)