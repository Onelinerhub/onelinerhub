# How can I connect a Laravel application to a database using PHP?
// plain

You can connect a Laravel application to a database using PHP by using the `DB` facade. The DB facade provides methods for interacting with your database.

For example, to connect to a MySQL database, you can use the `connect` method:

```php
$connection = DB::connect('mysql://user:password@hostname/database');
```

This will return a `PDO` instance connected to the given database.

You can also use the `select` method to run a query and get the results:

```php
$users = DB::select('select * from users');
```

The `$users` variable will contain an array of objects with the results of the query.

You can also use the `insert`, `update`, and `delete` methods to perform those operations on the database.

Here are some useful links for more information:

- [Database: Getting Started](https://laravel.com/docs/7.x/database)
- [Database: Query Builder](https://laravel.com/docs/7.x/queries)
- [Database: Migrations](https://laravel.com/docs/7.x/migrations)

onelinerhub: [How can I connect a Laravel application to a database using PHP?](https://onelinerhub.com/php-laravel/how-can-i-connect-a-laravel-application-to-a-database-using-php)