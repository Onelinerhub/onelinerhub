# How to use Swagger with Symfony and PHP?
// plain

Swagger is a popular open source framework for creating and documenting APIs. It can be used with Symfony and PHP to create a powerful and easy to use API.

To use Swagger with Symfony and PHP, first install the Swagger library using Composer:

```
composer require zircote/swagger-php
```

Then, create a Swagger file in the root of your project, for example `swagger.yaml`:

```
swagger: '2.0'
info:
  version: 1.0.0
  title: My API
```

Next, create a controller to handle the API requests and use the Swagger library to generate the documentation:

```php
<?php

use Zircote\Swagger\Swagger;

class MyController
{
    public function indexAction()
    {
        $swagger = \Swagger\scan(__DIR__ . '/../');
        header('Content-Type: application/json');
        echo $swagger;
    }
}
```

The output of the above code will be a JSON representation of the Swagger file:

```json
{
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "My API"
  }
}
```

Finally, add the route to the controller in the `routing.yml` file:

```yaml
my_api:
    path:     /my-api
    defaults: { _controller: MyController::indexAction }
```

## Helpful links

- [Swagger Documentation](https://swagger.io/docs/)
- [zircote/swagger-php](https://github.com/zircote/swagger-php)

onelinerhub: [How to use Swagger with Symfony and PHP?](https://onelinerhub.com/php-symfony/how-to-use-swagger-with-symfony-and-php)