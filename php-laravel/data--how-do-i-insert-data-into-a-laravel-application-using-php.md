# data

How do I insert data into a Laravel application using PHP?
// plain

To insert data into a Laravel application using PHP, you can use the `create` method on the Eloquent model. This method will create a new record in the database and return the model instance. For example:

```php
$user = User::create([
    'name' => 'John Doe',
    'email' => 'john@example.com',
    'password' => bcrypt('password')
]);
```

This code will create a new user record in the database with the provided name, email, and hashed password.

The parts of the code are:
- `User`: The Eloquent model.
- `create`: The method used to create a new record in the database.
- `name`, `email`, `password`: The attributes to set on the model instance.
- `bcrypt`: The function used to hash the password before inserting it into the database.

## Helpful links
- [Laravel Eloquent](https://laravel.com/docs/7.x/eloquent)
- [Laravel Bcrypt](https://laravel.com/docs/7.x/hashing#introduction)

onelinerhub: [data

How do I insert data into a Laravel application using PHP?](https://onelinerhub.com/php-laravel/data--how-do-i-insert-data-into-a-laravel-application-using-php)