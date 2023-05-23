# How to create a "Hello World" in PHP Symfony?
// plain

Creating a "Hello World" in PHP Symfony is a simple task.

## Example code

```
<?php

namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;

class HelloWorldController
{
    public function helloWorld()
    {
        return new Response('Hello World!');
    }
}
```

## Output example

```
Hello World!
```

## Code explanation

- `namespace App\Controller;` - declares the namespace of the controller
- `use Symfony\Component\HttpFoundation\Response;` - imports the Response class from the Symfony HttpFoundation component
- `class HelloWorldController` - declares the controller class
- `public function helloWorld()` - declares the helloWorld method
- `return new Response('Hello World!');` - returns a new Response object with the string "Hello World!"

## Helpful links
- [Symfony Documentation - Controllers](https://symfony.com/doc/current/controller.html)
- [Symfony Documentation - HttpFoundation Component](https://symfony.com/doc/current/components/http_foundation.html)

onelinerhub: [How to create a "Hello World" in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-a--hello-world--in-php-symfony)