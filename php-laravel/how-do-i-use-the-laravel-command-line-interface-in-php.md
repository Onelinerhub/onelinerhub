# How do I use the Laravel command line interface in PHP?
// plain

The Laravel command line interface (CLI) is a powerful tool that can be used to interact with your Laravel application. It is used to perform tasks such as running migrations, running tests, and creating new applications.

To use the Laravel CLI, you must first install it. To do this, you can use Composer. For example, you can run the following command to install the CLI:

```
composer global require laravel/installer
```

Once the CLI is installed, you can use it to interact with your Laravel application. For example, you can use the `artisan` command to run migrations, create new models, and run tests:

```
php artisan migrate
```

The output of the above command might look something like this:

```
Migration table created successfully.
Migrated: 2015_01_01_000000_create_users_table
Migrated: 2015_01_02_000000_create_posts_table
```

The Laravel CLI also provides other useful commands such as `make` and `serve`. The `make` command can be used to create new controllers, jobs, and other classes. The `serve` command can be used to start a local development server.

For more information about the Laravel CLI, you can refer to the [official documentation](https://laravel.com/docs/7.x/artisan).

onelinerhub: [How do I use the Laravel command line interface in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-command-line-interface-in-php)