# How to update an entity in PHP Symfony?
// plain

Updating an entity in PHP Symfony is a simple process.

First, you need to retrieve the entity from the database using the EntityManager.

```php
$em = $this->getDoctrine()->getManager();
$entity = $em->getRepository('AppBundle:EntityName')->find($id);
```

Then, you can update the entity's properties.

```php
$entity->setPropertyName('New Value');
```

Finally, you need to persist the changes to the database.

```php
$em->persist($entity);
$em->flush();
```

## Helpful links

- [Doctrine EntityManager](https://www.doctrine-project.org/projects/doctrine-orm/en/2.6/reference/working-with-objects.html#working-with-objects)
- [Symfony Documentation](https://symfony.com/doc/current/doctrine.html)

onelinerhub: [How to update an entity in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-update-an-entity-in-php-symfony)