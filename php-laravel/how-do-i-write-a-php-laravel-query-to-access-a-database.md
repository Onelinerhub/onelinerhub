# How do I write a PHP Laravel query to access a database?
// plain

To write a PHP Laravel query to access a database, you can use the Eloquent ORM. Eloquent is an Active Record implementation which allows you to interact with your database using an object-oriented syntax.

To use Eloquent, you must first define your database table using a model. For example, to define a model for a users table:

```php
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    //
}
```

Once you have defined your model, you can use it to query your database. For example, to get all users from the database:

```php
$users = App\User::all();
```

The output of this query will be a collection of `App\User` objects:

```
Illuminate\Database\Eloquent\Collection {#2913
  #items: array:2 [
    0 => App\User {#2910
      #fillable: array:2 [
        0 => "name"
        1 => "email"
      ]
      #table: "users"
      #connection: null
      #primaryKey: "id"
      #keyType: "int"
      #perPage: 15
      +incrementing: true
      +timestamps: true
      #attributes: array:3 [
        "id" => 1
        "name" => "John Doe"
        "email" => "john@example.com"
      ]
      #original: array:3 [
        "id" => 1
        "name" => "John Doe"
        "email" => "john@example.com"
      ]
      #relations: []
      #hidden: []
      #visible: []
      #appends: []
      #guarded: array:1 [
        0 => "*"
      ]
      #dates: []
      #dateFormat: null
      #casts: []
      #touches: []
      #observables: []
      #with: []
      #morphClass: null
      +exists: true
      +wasRecentlyCreated: false
    }
    1 => App\User {#2914
      #fillable: array:2 [
        0 => "name"
        1 => "email"
      ]
      #table: "users"
      #connection: null
      #primaryKey: "id"
      #keyType: "int"
      #perPage: 15
      +incrementing: true
      +timestamps: true
      #attributes: array:3 [
        "id" => 2
        "name" => "Jane Doe"
        "email" => "jane@example.com"
      ]
      #original: array:3 [
        "id" => 2
        "name" => "Jane Doe"
        "email" => "jane@example.com"
      ]
      #relations: []
      #hidden: []
      #visible: []
      #appends: []
      #guarded: array:1 [
        0 => "*"
      ]
      #dates: []
      #dateFormat: null
      #casts: []
      #touches: []
      #observables: []
      #with: []
      #morphClass: null
      +exists: true
      +wasRecentlyCreated: false
    }
  ]
}
```

You can also use Eloquent to query your database using more specific criteria. For example, to get all users with the name "John":

```php
$users = App\User::where('name', 'John')->get();
```

The output of this query will be a collection of `App\User` objects with the name "John":

```
Illuminate\Database\Eloquent\Collection {#2913
  #items: array:1 [
    0 => App\User {#2910
      #fillable: array:2 [
        0 => "name"
        1 => "email"
      ]
      #table: "users"
      #connection: null
      #primaryKey: "id"
      #keyType: "int"
      #perPage: 15
      +incrementing: true
      +timestamps: true
      #attributes: array:3 [
        "id" => 1
        "name" => "John Doe"
        "email" => "john@example.com"
      ]
      #original: array:3 [
        "id" => 1
        "name" => "John Doe"
        "email" => "john@example.com"
      ]
      #relations: []
      #hidden: []
      #visible: []
      #appends: []
      #guarded: array:1 [
        0 => "*"
      ]
      #dates: []
      #dateFormat: null
      #casts: []
      #touches: []
      #observables: []
      #with: []
      #morphClass: null
      +exists: true
      +wasRecentlyCreated: false
    }
  ]
}
```

## Helpful links

- [Laravel Eloquent Documentation](https://laravel.com/docs/7.x/eloquent)
- [Laravel Database Queries](https://laravel.com/docs/7.x/queries)

onelinerhub: [How do I write a PHP Laravel query to access a database?](https://onelinerhub.com/php-laravel/how-do-i-write-a-php-laravel-query-to-access-a-database)