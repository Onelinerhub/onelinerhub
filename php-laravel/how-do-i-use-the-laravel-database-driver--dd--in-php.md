# How do I use the Laravel Database Driver (DD) in PHP?
// plain

The Laravel Database Driver (DD) is a powerful tool for managing databases in PHP. It is a lightweight, yet powerful, object-oriented database abstraction layer which provides an easy-to-use interface for working with databases.

To use the Laravel Database Driver in PHP, you need to include the following code in your project:

```php
use Illuminate\Database\Capsule\Manager as Capsule;

$capsule = new Capsule;

$capsule->addConnection([
    'driver'    => 'mysql',
    'host'      => 'localhost',
    'database'  => 'database_name',
    'username'  => 'username',
    'password'  => 'password',
    'charset'   => 'utf8',
    'collation' => 'utf8_unicode_ci',
    'prefix'    => '',
]);

$capsule->setAsGlobal();

$capsule->bootEloquent();
```

This code will create a connection to the database. To query the database, you can use the `Capsule` class. For example, to select all rows from a table called `users`:

```php
$users = Capsule::table('users')->get();

print_r($users);
```

The output of this code will be an array of objects containing the data from the `users` table.

The Laravel Database Driver also provides additional features such as transactions, prepared statements, and query logging.

## Helpful links

- [Laravel Database Driver Documentation](https://laravel.com/docs/master/database)
- [Database: Getting Started](https://laravel.com/docs/master/database#getting-started)

onelinerhub: [How do I use the Laravel Database Driver (DD) in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-database-driver--dd--in-php)