# How do I set up a foreign key relationship in Laravel using PHP?
// plain

A foreign key relationship in Laravel can be set up using PHP by defining the relationship in the model class.

For example, to set up a foreign key relationship between a `User` and `Post` model, the following code can be used:

```
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    public function user()
    {
        return $this->belongsTo('App\User');
    }
}
```

In this example, the `belongsTo` method is used to define the foreign key relationship between the `Post` and `User` models.

## Code explanation

1. `namespace App;` - this defines the namespace of the model class.
2. `use Illuminate\Database\Eloquent\Model;` - this imports the `Model` class from the `Illuminate\Database\Eloquent` namespace.
3. `public function user()` - this defines the foreign key relationship between the `Post` and `User` models.
4. `return $this->belongsTo('App\User');` - this specifies the foreign key relationship between the `Post` and `User` models.

## Helpful links
- [Laravel Documentation - Eloquent Relationships](https://laravel.com/docs/7.x/eloquent-relationships)
- [Laravel Documentation - Defining Relationships](https://laravel.com/docs/7.x/eloquent-relationships#defining-relationships)

onelinerhub: [How do I set up a foreign key relationship in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-set-up-a-foreign-key-relationship-in-laravel-using-php)