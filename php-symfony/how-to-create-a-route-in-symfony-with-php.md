# How to create a route in Symfony with PHP?
// plain

Creating a route in Symfony with PHP is a simple process.

```
// src/Controller/BlogController.php

/**
 * @Route("/blog")
 */
public function list()
{
    // ...
}
```

The code above will create a route for the `list()` method in the `BlogController` class.

The parts of the code are:

- `@Route`: This is an annotation that tells Symfony to create a route for the method.
- `"/blog"`: This is the path of the route.
- `public function list()`: This is the method that will be called when the route is accessed.

## Helpful links

- [Routing](https://symfony.com/doc/current/routing.html)
- [Controller](https://symfony.com/doc/current/controller.html)

onelinerhub: [How to create a route in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-create-a-route-in-symfony-with-php)