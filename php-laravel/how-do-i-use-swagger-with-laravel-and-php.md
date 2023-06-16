# How do I use Swagger with Laravel and PHP?
// plain

Swagger is an open-source tool used to generate documentation for APIs. It can be used with Laravel and PHP to create an interactive API reference. This reference can be used to test and debug API calls.

To use Swagger with Laravel and PHP, you will need to install the Swaggervel package. This package provides an easy way to integrate Swagger into your Laravel application.

## Example code

```
composer require darkaonline/l5-swagger
```

Once the package is installed, you will need to edit the config/app.php file and add the following line to the providers array:
```
Darkaonline\L5Swagger\L5SwaggerServiceProvider::class,
```

You can then publish the Swagger configuration file by running the following command:
```
php artisan vendor:publish --provider="Darkaonline\L5Swagger\L5SwaggerServiceProvider"
```

After the configuration file has been published, you will need to generate the Swagger JSON file. This can be done by running the following command:
```
php artisan l5-swagger:generate
```

Finally, you can view the interactive API reference by visiting the `/api/documentation` route in your application.

## Code explanation

- `composer require darkaonline/l5-swagger`: Installs the Swaggervel package.
- `Darkaonline\L5Swagger\L5SwaggerServiceProvider::class`: Adds the Swagger Service Provider to the config/app.php file.
- `php artisan vendor:publish --provider="Darkaonline\L5Swagger\L5SwaggerServiceProvider"`: Publishes the Swagger configuration file.
- `php artisan l5-swagger:generate`: Generates the Swagger JSON file.

## Helpful links
- [Swagger Documentation](https://swagger.io/docs/)
- [Swaggervel Package](https://github.com/DarkaOnLine/L5-Swagger)

onelinerhub: [How do I use Swagger with Laravel and PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-swagger-with-laravel-and-php)