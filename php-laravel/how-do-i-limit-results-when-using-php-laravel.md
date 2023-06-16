# How do I limit results when using PHP Laravel?
// plain

Limiting results when using PHP Laravel can be done using the `take()` and `skip()` methods.

The `take()` method is used to limit the number of results that are returned from a query. For example, the following code:
```
$users = User::take(10)->get();
```
Will return the first 10 results from the query.

The `skip()` method is used to skip a certain number of results from a query. For example, the following code:
```
$users = User::skip(10)->get();
```
Will skip the first 10 results from the query and return the remaining results.

These methods can also be chained together to limit and skip results in a single query. For example, the following code:
```
$users = User::take(10)->skip(10)->get();
```
Will skip the first 10 results and return the next 10 results from the query.

It is also possible to limit the number of results returned from a query using the `limit()` method. For example, the following code:
```
$users = User::limit(10)->get();
```
Will return the first 10 results from the query.

## Helpful links

- [Laravel Documentation: Retrieving Results](https://laravel.com/docs/5.7/queries#retrieving-results)
- [Laravel Documentation: Pagination](https://laravel.com/docs/5.7/pagination)

onelinerhub: [How do I limit results when using PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-limit-results-when-using-php-laravel)