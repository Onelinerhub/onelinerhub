# How to create a backend with PHP Symfony?
// plain

Creating a backend with PHP Symfony is easy and straightforward.

1. Install the Symfony framework:
```
$ composer create-project symfony/website-skeleton my-project
```

2. Create a controller:
```
<?php

namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;

class DefaultController
{
    public function index()
    {
        return new Response('Hello World!');
    }
}
```

3. Create a route:
```
# config/routes.yaml

index:
    path: /
    controller: App\Controller\DefaultController::index
```

4. Start the server:
```
$ cd my-project
$ symfony server:start
```

5. Visit the page:
```
http://localhost:8000
```

You should now see the "Hello World!" message.

## Helpful links
- [Symfony Documentation](https://symfony.com/doc/current/index.html)
- [Getting Started with Symfony](https://symfony.com/doc/current/setup.html)

onelinerhub: [How to create a backend with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-a-backend-with-php-symfony)