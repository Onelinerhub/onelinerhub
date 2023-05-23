# How to create a project in PHP Symfony?
// plain

Creating a project in PHP Symfony is easy and straightforward.

1. Install the Symfony binary using the [installer](https://symfony.com/download) or [Composer](https://getcomposer.org/).

2. Create a new project using the `symfony new` command:
```
$ symfony new my_project
```

3. Configure the database connection in the `.env` file:
```
DATABASE_URL=mysql://db_user:db_password@127.0.0.1:3306/db_name
```

4. Create the database using the `doctrine:database:create` command:
```
$ php bin/console doctrine:database:create
```

5. Start the built-in web server:
```
$ php bin/console server:run
```

Your project is now ready to use.

onelinerhub: [How to create a project in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-a-project-in-php-symfony)