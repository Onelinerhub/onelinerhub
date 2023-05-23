# PHP Symfony build app example
// plain

Symfony is a popular PHP framework for building web applications. It provides a set of reusable components and a structured framework for creating complex web applications.

The following example shows how to create a simple Symfony application:

```
$ composer create-project symfony/skeleton my_project
$ cd my_project
$ php bin/console server:run
```

This will create a new project directory called `my_project` and start a local web server. You can then access the application at `http://localhost:8000`.

The code above consists of the following parts:

1. `composer create-project symfony/skeleton my_project`: This command creates a new Symfony project in the `my_project` directory.

2. `cd my_project`: This command changes the current working directory to the newly created project directory.

3. `php bin/console server:run`: This command starts a local web server and makes the application available at `http://localhost:8000`.

For more information about creating Symfony applications, see the [official documentation](https://symfony.com/doc/current/setup.html).

onelinerhub: [PHP Symfony build app example](https://onelinerhub.com/php-symfony/php-symfony-build-app-example)