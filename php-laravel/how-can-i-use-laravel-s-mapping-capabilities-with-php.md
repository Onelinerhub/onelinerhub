# How can I use Laravel's mapping capabilities with PHP?
// plain

Laravel's mapping capabilities can be used with PHP to create powerful web applications. Laravel provides various features such as Eloquent ORM, query builder, routing, and authentication.

Using the Eloquent ORM, you can write PHP code to map objects to database tables and perform various database operations such as insert, update, delete, etc.

For example, you can use Eloquent ORM to create a model for a database table and use it to perform database operations.

```
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    protected $table = 'users';
    protected $fillable = ['name', 'email'];
}

$user = User::create([
    'name' => 'John Doe',
    'email' => 'john@example.com'
]);

echo $user->name; // John Doe
```

In addition, you can use the query builder to write SQL queries in PHP and perform various database operations.

```
<?php

$user = DB::table('users')->where('name', 'John Doe')->first();

echo $user->name; // John Doe
```

You can also use routing to define routes for your application and authentication to authenticate users.

## Code explanation

- `namespace App;`: defines the namespace of the model
- `use Illuminate\Database\Eloquent\Model;`: imports the Eloquent Model class
- `protected $table = 'users';`: defines the database table for the model
- `protected $fillable = ['name', 'email'];`: defines the fields that can be filled
- `User::create()`: creates a new user record
- `DB::table('users')->where('name', 'John Doe')->first()`: fetches the user record with the name "John Doe"

## Helpful links
- [Laravel Eloquent ORM](https://laravel.com/docs/7.x/eloquent)
- [Laravel Query Builder](https://laravel.com/docs/7.x/queries)
- [Laravel Routing](https://laravel.com/docs/7.x/routing)
- [Laravel Authentication](https://laravel.com/docs/7.x/authentication)

onelinerhub: [How can I use Laravel's mapping capabilities with PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-s-mapping-capabilities-with-php)