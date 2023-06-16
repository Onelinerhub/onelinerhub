# How do I use the Laravel Find function in PHP?
// plain

The Laravel Find function is a powerful tool that allows you to retrieve a record from a database using its primary key. This function is part of the Eloquent ORM, which is included with the Laravel framework.

## Example code

```
$user = User::find(1);
```

This code will retrieve the record from the `users` table in the database that has the primary key of `1`. If the record exists, it will be returned as an instance of the `User` model.

The Find function can also accept an array of primary keys. For example, the following code will retrieve all records from the `users` table with primary keys of `1` and `2`:

```
$users = User::find([1, 2]);
```

This code will return an array of `User` model instances, one for each record that was found.

## Helpful links

- [Laravel Documentation - Eloquent ORM](https://laravel.com/docs/7.x/eloquent)
- [Laravel Documentation - Retrieving Single Models](https://laravel.com/docs/7.x/eloquent#retrieving-single-models)

onelinerhub: [How do I use the Laravel Find function in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-find-function-in-php)