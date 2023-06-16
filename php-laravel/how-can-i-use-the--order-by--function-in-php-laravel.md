# How can I use the "order by" function in PHP Laravel?
// plain

The `order by` function in PHP Laravel can be used to sort the result set of a query in ascending or descending order. This is a very useful feature when you want to perform certain operations on the data in the database.

## Example code

```
$users = User::orderBy('name', 'asc')->get();
```

This code will return a collection of all users in ascending order based on their name.

Parts of the code:
* `User`: The model from which the data is being retrieved.
* `orderBy`: The method used to sort the results.
* `name`: The column on which the sorting is done.
* `asc`: The sorting direction (ascending or descending).

## Helpful links
* [Laravel Documentation - Querying Builder](https://laravel.com/docs/7.x/queries#ordering-results)
* [Laravel Documentation - Eloquent ORM](https://laravel.com/docs/7.x/eloquent)

onelinerhub: [How can I use the "order by" function in PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-the--order-by--function-in-php-laravel)