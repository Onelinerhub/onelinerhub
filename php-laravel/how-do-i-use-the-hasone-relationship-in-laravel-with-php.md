# How do I use the hasOne relationship in Laravel with PHP?
// plain

The `hasOne` relationship in Laravel with PHP allows one model to be related to another model. It is used to define a one-to-one relationship between two models.

For example, if a User model has one Profile model, we can define the relationship like this:

```php
class User extends Model
{
    public function profile()
    {
        return $this->hasOne('App\Profile');
    }
}
```

Then, we can access the related model by using the `profile` method:

```php
$user = App\User::find(1);

echo $user->profile->name;
// Output: John Doe
```

The following parts are included in the example code above:

- `class User extends Model`: This is the User model class which extends the base Model class provided by Laravel.

- `public function profile()`: This is the method used to define the relationship.

- `return $this->hasOne('App\Profile');`: This is the statement used to define the relationship between the User and Profile models.

- `$user = App\User::find(1);`: This is the statement used to retrieve a single User model from the database.

- `echo $user->profile->name;`: This is the statement used to access the related Profile model's name property.

For more information about the `hasOne` relationship, please refer to the [Laravel documentation](https://laravel.com/docs/7.x/eloquent-relationships#one-to-one).

onelinerhub: [How do I use the hasOne relationship in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-hasone-relationship-in-laravel-with-php)