# How do I use the Laravel BelongsTo relationship in PHP?
// plain

The Laravel BelongsTo relationship is a type of Eloquent relationship that is used to define a relationship between two models. It is used to specify that a model belongs to a single other model.

For example, if you have a User model and a Post model, you would use the BelongsTo relationship to specify that a Post belongs to a single User.

```
class Post extends Model
{
    public function user()
    {
        return $this->belongsTo('App\User');
    }
}
```

Then, you can access the related User model from a Post instance:

```
$post = Post::find(1);
$user = $post->user;
```

The above code will return the related User model instance from the Post instance.

The BelongsTo relationship also allows you to specify the foreign key and the local key for the relationship:

```
class Post extends Model
{
    public function user()
    {
        return $this->belongsTo('App\User', 'foreign_key', 'other_key');
    }
}
```

## Helpful links

- [Laravel Documentation - Eloquent Relationships](https://laravel.com/docs/7.x/eloquent-relationships)
- [Laravel Documentation - BelongsTo Relationship](https://laravel.com/docs/7.x/eloquent-relationships#one-to-one)

onelinerhub: [How do I use the Laravel BelongsTo relationship in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-belongsto-relationship-in-php)