# data

How do I retrieve data using PHP and Laravel?
// plain

Retrieving data using PHP and Laravel is relatively straightforward. The following example code block demonstrates how to use the Eloquent ORM to retrieve data from a database table:

```php
$users = User::all();
```

This code will return a collection of all the records in the `users` table.

The code consists of the following parts:

1. `User`: This is the model class that is associated with the `users` table.
2. `all()`: This is a static method that is used to retrieve all the records from the table.

In addition to retrieving data, Eloquent also provides other useful methods for working with data such as `find()`, `where()`, `update()`, and `delete()`. For more information, please refer to the [Laravel Documentation](https://laravel.com/docs/6.x/eloquent).

onelinerhub: [data

How do I retrieve data using PHP and Laravel?](https://onelinerhub.com/php-laravel/data--how-do-i-retrieve-data-using-php-and-laravel)