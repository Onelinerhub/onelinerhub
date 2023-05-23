# How to use the PHP Symfony factory?
// plain

The PHP Symfony factory is a powerful tool for creating objects in a structured and organized way. It allows developers to create objects with a single line of code, and to easily customize the objects with additional parameters.

## Example

```
$factory = new \Symfony\Component\DependencyInjection\ContainerBuilder();
$factory->register('my_object', 'MyObject');
$myObject = $factory->get('my_object');
```

This example creates an instance of the `MyObject` class and stores it in the `$myObject` variable.

## Code explanation


1. `$factory = new \Symfony\Component\DependencyInjection\ContainerBuilder();` - This creates a new instance of the `ContainerBuilder` class, which is used to register and retrieve objects.

2. `$factory->register('my_object', 'MyObject');` - This registers the `MyObject` class with the `ContainerBuilder` instance, using the identifier `my_object`.

3. `$myObject = $factory->get('my_object');` - This retrieves the `MyObject` instance from the `ContainerBuilder` instance, using the identifier `my_object`.

## Helpful links

- [Symfony Documentation - Dependency Injection](https://symfony.com/doc/current/components/dependency_injection.html)
- [Symfony Documentation - ContainerBuilder](https://symfony.com/doc/current/components/dependency_injection/container_builder.html)

onelinerhub: [How to use the PHP Symfony factory?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-factory)