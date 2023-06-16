# How do I set up a Laravel HasMany relationship using PHP?
// plain

To set up a Laravel HasMany relationship using PHP, you'll need to use the `hasMany()` method. This method takes two arguments: the name of the related model, and the foreign key of the parent model.

For example, if you're setting up a relationship between a `User` model and a `Post` model, the `User` model would have the `hasMany()` method:

```php
public function posts()
{
    return $this->hasMany('App\Post', 'user_id');
}
```

The first argument is the name of the related model, `App\Post`, and the second argument is the foreign key, `user_id`. This tells the `User` model that it has many `Post` models, and the foreign key is `user_id`.

Once the relationship is set up, you can use the `posts` method to access the related `Post` models:

```php
$user = App\User::find(1);

foreach ($user->posts as $post) {
    echo $post->title;
}
```

This will output the title of each `Post` model related to the `User` model.

### Code Parts

1. `hasMany()` method: This method takes two arguments: the name of the related model, and the foreign key of the parent model.
2. `posts()` method: This tells the `User` model that it has many `Post` models, and the foreign key is `user_id`.
3. `posts` method: This will output the title of each `Post` model related to the `User` model.

### Relevant Links

- [Laravel Documentation - Eloquent Relationships](https://laravel.com/docs/7.x/eloquent-relationships)
- [Laracasts - Eloquent: Relationships](https://laracasts.com/series/laravel-from-scratch-2018/episodes/19)

onelinerhub: [How do I set up a Laravel HasMany relationship using PHP?](https://onelinerhub.com/php-laravel/how-do-i-set-up-a-laravel-hasmany-relationship-using-php)