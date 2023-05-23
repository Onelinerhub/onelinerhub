# How to create a migration in PHP Symfony?
// plain

Creating a migration in PHP Symfony is a simple process.

Create a migration class in the `src/Migrations` directory:
```php
<?php

namespace App\Migrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20200101000000 extends AbstractMigration
{
    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
    }
}
```

Generate the SQL code for the migration:
```
$ php bin/console doctrine:migrations:diff
```

Execute the migration:
```
$ php bin/console doctrine:migrations:migrate
```

Check the status of the migration:
```
$ php bin/console doctrine:migrations:status
```

Revert the migration if needed:
```
$ php bin/console doctrine:migrations:migrate prev
```

## Helpful links
- [Doctrine Migrations Documentation](https://www.doctrine-project.org/projects/doctrine-migrations/en/latest/reference/introduction.html)
- [Symfony Documentation - Doctrine Migrations](https://symfony.com/doc/current/bundles/DoctrineMigrationsBundle/index.html)

onelinerhub: [How to create a migration in PHP Symfony?
](https://onelinerhub.com/php-symfony/how-to-create-a-migration-in-php-symfony)
