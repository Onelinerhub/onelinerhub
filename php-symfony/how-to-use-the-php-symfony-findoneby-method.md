# How to use the PHP Symfony findOneBy method?
// plain

The `findOneBy` method is a part of the Symfony Doctrine Query Builder and is used to retrieve a single entity from the database. It takes an array of criteria as its first argument and an array of orderings as its second argument.

## Example

```
$user = $em->getRepository('AppBundle:User')
    ->findOneBy(
        array('username' => 'johndoe'),
        array('id' => 'DESC')
    );
```

## Output example

```
Object(AppBundle\Entity\User)#123 (...)
```

## Code explanation

- `$em`: Entity Manager object, used to access the database.
- `getRepository`: Method of the Entity Manager, used to access the repository of a given entity.
- `findOneBy`: Method of the repository, used to retrieve a single entity from the database.
- `array('username' => 'johndoe')`: Criteria used to filter the entities.
- `array('id' => 'DESC')`: Ordering used to sort the entities.

## Helpful links
- [Doctrine Query Builder](https://www.doctrine-project.org/projects/doctrine-orm/en/2.6/reference/query-builder.html)
- [Symfony Documentation - Doctrine Query Builder](https://symfony.com/doc/current/doctrine.html#querying-for-objects-the-querybuilder)

onelinerhub: [How to use the PHP Symfony findOneBy method?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-findoneby-method)