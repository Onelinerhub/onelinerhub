# How do I run a seeder in Laravel using PHP?
// plain

To run a seeder in Laravel using PHP, you can use the `php artisan db:seed` command. This command will run the `DatabaseSeeder` class, which is located in the `database/seeds` directory.

```
php artisan db:seed
```

This command will run all the seeders that are listed in the `DatabaseSeeder` class. You can also run a specific seeder class by using the `--class` option.

```
php artisan db:seed --class=UsersTableSeeder
```

The above command will run the `UsersTableSeeder` class. If the seeder class is successful, you will see the following output:

```
Seeded: UsersTableSeeder
```

You can also pass additional options to the seeder class by using the `--option` option.

```
php artisan db:seed --class=UsersTableSeeder --option=value
```

The options that are available to you depend on the seeder class that you are running.

### List of code parts and explanation

1. `php artisan db:seed` - This command will run the `DatabaseSeeder` class, which is located in the `database/seeds` directory.
2. `php artisan db:seed --class=UsersTableSeeder` - This command will run the `UsersTableSeeder` class.
3. `php artisan db:seed --class=UsersTableSeeder --option=value` - This command will run the `UsersTableSeeder` class and pass additional options to the seeder class.

### List of relevant links

- [Laravel Database Seeding](https://laravel.com/docs/7.x/seeding)
- [Database Seeder](https://laravel.com/docs/7.x/database#database-seeding)

onelinerhub: [How do I run a seeder in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-run-a-seeder-in-laravel-using-php)