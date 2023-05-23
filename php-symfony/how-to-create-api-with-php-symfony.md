# How to create API with PHP Symfony?
// plain

Creating an API with PHP Symfony is a straightforward process.

First, create a new Symfony project using the command line:
```
composer create-project symfony/website-skeleton my-project
```

This will create a new project in the `my-project` directory.

Next, install the API Platform bundle:
```
composer require api
```

This will install the necessary components for creating an API.

Then, create the entity classes for the API:
```
php bin/console make:entity
```

This will create the necessary classes for the API.

Finally, configure the API routes:
```
api:swagger:export
```

This will create the routes for the API.

These steps will create a basic API with PHP Symfony. For more information, see the [Symfony documentation](https://symfony.com/doc/current/index.html).

onelinerhub: [How to create API with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-api-with-php-symfony)