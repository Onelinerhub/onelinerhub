# How can I use Laravel Eloquent to group data by a specific field in PHP?
// plain

Using Laravel Eloquent, you can group data by a specific field in PHP by using the `groupBy()` method.

Here is an example:
```
$users = User::groupBy('country')->get();
```

This will return a collection of users grouped by their country.

Here is a breakdown of the code:
- `User::`: This is the Eloquent model that is used to query the database.
- `groupBy('country')`: This is the method used to group the data by the specified field.
- `get()`: This is the method used to retrieve the data from the database.

For more information, see the [Laravel Documentation](https://laravel.com/docs/7.x/eloquent#retrieving-groups-of-column-values).

onelinerhub: [How can I use Laravel Eloquent to group data by a specific field in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-eloquent-to-group-data-by-a-specific-field-in-php)