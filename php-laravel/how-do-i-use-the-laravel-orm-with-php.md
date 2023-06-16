# How do I use the Laravel ORM with PHP?
// plain

The Laravel ORM (Object-Relational Mapping) is an advanced feature of the Laravel PHP framework that allows developers to easily interact with databases. It provides an easy-to-use interface for retrieving and manipulating data stored in a database.

To use the Laravel ORM, you must first create a model class for each database table you wish to interact with. The model class will contain methods for retrieving and manipulating data from the database.

For example, to create a model class for a `users` table:

```php
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    //
}
```

Once the model class is created, you can use the model to retrieve and manipulate data from the `users` table. For example, to retrieve all users from the `users` table:

```php
<?php

use App\User;

$users = User::all();

foreach ($users as $user) {
    echo $user->name;
}
```

The Laravel ORM also provides additional methods for retrieving and manipulating data, such as `find()`, `where()`, `orderBy()`, `update()`, `create()`, and `delete()`.

For more information about using the Laravel ORM, please refer to the [Laravel Documentation](https://laravel.com/docs/7.x/eloquent).

onelinerhub: [How do I use the Laravel ORM with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-orm-with-php)