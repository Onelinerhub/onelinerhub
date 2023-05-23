# How to generate a model in PHP Symfony?
// plain

Generating a model in PHP Symfony is a simple process.

1. Create a new model class in the `src/Entity` directory:

```php
<?php

namespace App\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass="App\Repository\MyModelRepository")
 */
class MyModel
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

2. Generate the getters and setters for the model:

```
php bin/console make:entity --regenerate App
```

3. Create the database table for the model:

```
php bin/console doctrine:schema:update --force
```

4. Create a repository class for the model:

```php
<?php

namespace App\Repository;

use App\Entity\MyModel;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Symfony\Bridge\Doctrine\RegistryInterface;

/**
 * @method MyModel|null find($id, $lockMode = null, $lockVersion = null)
 * @method MyModel|null findOneBy(array $criteria, array $orderBy = null)
 * @method MyModel[]    findAll()
 * @method MyModel[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class MyModelRepository extends ServiceEntityRepository
{
    public function __construct(RegistryInterface $registry)
    {
        parent::__construct($registry, MyModel::class);
    }

    // ...
}
```

5. Use the model in your application.

## Helpful links

- [Doctrine ORM](https://www.doctrine-project.org/projects/orm.html)
- [Symfony Documentation - Generating an Entity Class](https://symfony.com/doc/current/doctrine.html#generating-an-entity-class)

onelinerhub: [How to generate a model in PHP Symfony?
](https://onelinerhub.com/php-symfony/how-to-generate-a-model-in-php-symfony)
