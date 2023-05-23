# How to use ORM in PHP Symfony?
// plain

ORM (Object Relational Mapping) is a way to map objects in a program to database tables. It is used in Symfony to simplify the process of interacting with a database.

## Example code

```php
// Create a new entity
$entity = new Entity();

// Set the entity's properties
$entity->setName('John Doe');
$entity->setAge(30);

// Save the entity to the database
$entity->save();
```

## Output example

```
Entity saved successfully.
```

## Code explanation

- `$entity = new Entity();` - creates a new entity object
- `$entity->setName('John Doe');` - sets the name property of the entity
- `$entity->setAge(30);` - sets the age property of the entity
- `$entity->save();` - saves the entity to the database

## Helpful links
- [Symfony ORM Documentation](https://symfony.com/doc/current/doctrine.html)
- [Doctrine ORM Documentation](https://www.doctrine-project.org/projects/doctrine-orm/en/2.7/index.html)

onelinerhub: [How to use ORM in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-orm-in-php-symfony)