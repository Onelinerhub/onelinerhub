# How to create a controller using the Symfony console in PHP?
// plain

Creating a controller using the Symfony console in PHP is a simple process.

First, create a new controller class in the `src/Controller` directory:
```php
<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;

class MyController extends AbstractController
{
    // ...
}
```

Then, generate the routes for the controller using the `make:controller` command:
```
$ php bin/console make:controller MyController
```

This will generate the routes for the controller and add them to the `config/routes.yaml` file.

## Code explanation


1. Create a new controller class in the `src/Controller` directory.
2. Generate the routes for the controller using the `make:controller` command.
3. Add the routes to the `config/routes.yaml` file.

## Helpful links

- [Symfony Console](https://symfony.com/doc/current/console.html)
- [Creating a Controller](https://symfony.com/doc/current/controller.html)

onelinerhub: [How to create a controller using the Symfony console in PHP?](https://onelinerhub.com/php-symfony-console/how-to-create-a-controller-using-the-symfony-console-in-php)