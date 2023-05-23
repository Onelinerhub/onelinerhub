# How to create a PHP Symfony example project?
// plain

Creating a PHP Symfony example project is easy and straightforward.

1. Install the Symfony framework using the following command:
```
$ composer create-project symfony/website-skeleton my-project
```
2. Configure the database connection in the .env file:
```
DATABASE_URL=mysql://db_user:db_password@127.0.0.1:3306/db_name
```
3. Create the database:
```
$ php bin/console doctrine:database:create
```
4. Create the database schema:
```
$ php bin/console doctrine:schema:create
```
5. Run the Symfony server:
```
$ php bin/console server:run
```

The output should be:
```
 [OK] Server listening on http://127.0.0.1:8000
```

You have now successfully created a PHP Symfony example project.

## Helpful links

- [Symfony Documentation](https://symfony.com/doc/current/index.html)
- [Getting Started with Symfony](https://symfony.com/doc/current/setup.html)

onelinerhub: [How to create a PHP Symfony example project?](https://onelinerhub.com/php-symfony/how-to-create-a-php-symfony-example-project)