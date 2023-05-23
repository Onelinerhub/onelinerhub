# How to persist data in PHP Symfony?
// plain

Persisting data in PHP Symfony can be done using Doctrine ORM. Doctrine is an Object Relational Mapper (ORM) which allows developers to map objects to a database.

## Example code

```
$em = $this->getDoctrine()->getManager();
$user = new User();
$user->setName('John Doe');
$em->persist($user);
$em->flush();
```

This code will create a new user object and persist it to the database.

## Code explanation

- `$em = $this->getDoctrine()->getManager();` - This line gets the Entity Manager from the Doctrine service.
- `$user = new User();` - This line creates a new User object.
- `$user->setName('John Doe');` - This line sets the name of the user.
- `$em->persist($user);` - This line tells Doctrine to persist the user object to the database.
- `$em->flush();` - This line tells Doctrine to actually execute the query and persist the data.

## Helpful links
- [Doctrine ORM Documentation](https://www.doctrine-project.org/projects/doctrine-orm/en/2.7/index.html)
- [Symfony Doctrine Tutorial](https://symfony.com/doc/current/doctrine.html)

onelinerhub: [How to persist data in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-persist-data-in-php-symfony)