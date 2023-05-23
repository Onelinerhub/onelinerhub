# How to create a PHP Symfony entity?
// plain

Creating a PHP Symfony entity is a simple process.

First, create a new entity class in the `src/Entity` directory:
```php
<?php

namespace App\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass="App\Repository\MyEntityRepository")
 */
class MyEntity
{
    /**
     * @ORM\Id()
     * @ORM\GeneratedValue()
     * @ORM\Column(type="integer")
     */
    private $id;

    // ...
}
```

Next, generate the getters and setters for the entity:
```
php bin/console make:entity --regenerate
```

This will generate the getters and setters for the entity, allowing you to access and modify the entity's properties.

Finally, update the database schema to reflect the changes:
```
php bin/console doctrine:schema:update --force
```

This will update the database schema to reflect the changes made to the entity.

## Helpful links
- [Symfony Documentation - Creating an Entity Class](https://symfony.com/doc/current/doctrine.html#creating-an-entity-class)
- [Symfony Documentation - Generating Getters and Setters](https://symfony.com/doc/current/doctrine/reverse_engineering.html#generating-getters-and-setters)
- [Symfony Documentation - Updating the Database Schema](https://symfony.com/doc/current/doctrine/schema_update.html)

onelinerhub: [How to create a PHP Symfony entity?](https://onelinerhub.com/php-symfony/how-to-create-a-php-symfony-entity)