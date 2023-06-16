# How can I create a relationship between two models in Laravel using PHP?
// plain

Creating a relationship between two models in Laravel using PHP is done through Eloquent ORM. Eloquent ORM provides a simple ActiveRecord implementation for working with the database. The following example illustrates how to create a relationship between two models in Laravel using PHP:

```php
// Model A
class User extends Model
{
    public function posts()
    {
        return $this->hasMany('App\Post');
    }
}

// Model B
class Post extends Model
{
    public function user()
    {
        return $this->belongsTo('App\User');
    }
}
```

In the example, the `User` model has a `posts` method which defines a one-to-many relationship with the `Post` model. The `Post` model has a `user` method which defines a one-to-one relationship with the `User` model.

The following parts explain the example code:

- `User` model: defines a one-to-many relationship with the `Post` model.
- `posts` method: defines a one-to-many relationship.
- `Post` model: defines a one-to-one relationship with the `User` model.
- `user` method: defines a one-to-one relationship.

## Helpful links

- [Eloquent ORM](https://laravel.com/docs/7.x/eloquent)
- [Laravel Relationships](https://laravel.com/docs/7.x/eloquent-relationships)

onelinerhub: [How can I create a relationship between two models in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-can-i-create-a-relationship-between-two-models-in-laravel-using-php)