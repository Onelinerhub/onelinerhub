# How do I use the GROUP BY clause in a Laravel query using PHP?
// plain

The GROUP BY clause in Laravel can be used to group the results of a query according to specified criteria. This can be done using the query builder or Eloquent ORM.

##### Query Builder

Using the query builder, the GROUP BY clause can be added to a query by using the `groupBy()` method. For example:

```php
$users = DB::table('users')
            ->groupBy('age')
            ->get();
```

This will return all users grouped by age.

##### Eloquent ORM

Using Eloquent ORM, the GROUP BY clause can be added to a query by using the `groupBy()` method. For example:

```php
$users = User::groupBy('age')->get();
```

This will return all users grouped by age.

##### Explanation

- `DB::table('users')`: This will retrieve all records from the users table.
- `groupBy('age')`: This will group the records by the age column.
- `get()`: This will execute the query and return the results.

##### Relevant Links

- [Laravel - Query Builder - GROUP BY](https://laravel.com/docs/7.x/queries#grouping)
- [Laravel - Eloquent ORM - GROUP BY](https://laravel.com/docs/7.x/eloquent#querying-groups)

onelinerhub: [How do I use the GROUP BY clause in a Laravel query using PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-group-by-clause-in-a-laravel-query-using-php)