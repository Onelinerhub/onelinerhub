# How do I create a model in Laravel using PHP?
// plain

To create a model in Laravel using PHP, you can use the `php artisan make:model` command. This command will generate a new model class for you.

## Example code

```
php artisan make:model User
```

This will create a new `User.php` file in the `app` directory. This file will contain a class named `User` which will extend the `Model` class.

The `User` class will contain several methods that you can use to interact with the database. For example, you can use the `all()` method to fetch all records from the database.

You can also add custom methods to the `User` class. For example, you can add a `getFullName()` method to get the full name of a user.

```php
public function getFullName()
{
    return $this->first_name . ' ' . $this->last_name;
}
```

You can then use this method to get the full name of a user:

```php
$user = App\User::find(1);
echo $user->getFullName(); // Outputs "John Doe"
```

For more information, see the [Laravel Documentation](https://laravel.com/docs/7.x/eloquent).

onelinerhub: [How do I create a model in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-create-a-model-in-laravel-using-php)