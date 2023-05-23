# How to use dependency injection in Symfony with PHP?
// plain

Dependency Injection (DI) is a design pattern used to create loosely coupled components in a system. It is a powerful tool for managing class dependencies in Symfony with PHP.

To use DI in Symfony, you need to create a service container and register services in it. Services are objects that can be used by other objects in the system.

## Example code

```
// Create a service container
$container = new Symfony\Component\DependencyInjection\ContainerBuilder();

// Register a service
$container->register('my_service', 'My\Service\Class');

// Get the service
$myService = $container->get('my_service');
```

## Output example

```
My\Service\Class
```

## Code explanation

- `$container = new Symfony\Component\DependencyInjection\ContainerBuilder();` - creates a service container.
- `$container->register('my_service', 'My\Service\Class');` - registers a service in the container.
- `$myService = $container->get('my_service');` - gets the service from the container.

## Helpful links
- [Symfony Dependency Injection Component](https://symfony.com/doc/current/components/dependency_injection.html)
- [Dependency Injection in Symfony](https://www.sitepoint.com/dependency-injection-in-symfony/)

onelinerhub: [How to use dependency injection in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-use-dependency-injection-in-symfony-with-php)