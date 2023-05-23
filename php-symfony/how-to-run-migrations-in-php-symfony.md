# How to run migrations in PHP Symfony?
// plain

Migrations in Symfony are managed by the Doctrine Migrations Bundle. To run migrations, you need to install the bundle first.

```
composer require doctrine/doctrine-migrations-bundle
```

After the bundle is installed, you can run the migrations with the following command:

```
php bin/console doctrine:migrations:migrate
```

This command will execute all the migrations that have not been executed yet.

1. `composer require doctrine/doctrine-migrations-bundle` - installs the Doctrine Migrations Bundle
2. `php bin/console doctrine:migrations:migrate` - runs the migrations

## Helpful links

- [Doctrine Migrations Bundle](https://symfony.com/doc/master/bundles/DoctrineMigrationsBundle/index.html)
- [Doctrine Migrations Documentation](https://www.doctrine-project.org/projects/doctrine-migrations/en/latest/)

onelinerhub: [How to run migrations in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-run-migrations-in-php-symfony)