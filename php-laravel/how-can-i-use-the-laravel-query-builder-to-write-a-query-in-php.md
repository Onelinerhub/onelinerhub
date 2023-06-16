# How can I use the Laravel Query Builder to write a query in PHP?
// plain

Using the Laravel Query Builder, you can write a query in PHP using a few simple steps.

First, you need to include the Query Builder class in your PHP script:
```
use Illuminate\Database\Query\Builder;
```

Next, you need to create an instance of the Query Builder class:
```
$query = new Builder;
```

You can then use the Query Builder methods to build your query:
```
$query->select('*')->from('users')->where('name', 'John');
```

Finally, you can execute the query using the `get()` method:
```
$users = $query->get();
```

The output of the code above would be an array of users with the name "John".

The Laravel Query Builder provides a variety of methods to build queries. Here are some of the methods you can use:

- `select()`: Specifies which columns should be included in the query
- `from()`: Specifies which table the query should be run against
- `where()`: Specifies a condition that must be met for the query to be valid
- `orderBy()`: Specifies the order in which the query results should be returned
- `get()`: Executes the query and returns the results

For more information on the Laravel Query Builder, please see the [Laravel documentation](https://laravel.com/docs/master/queries).

onelinerhub: [How can I use the Laravel Query Builder to write a query in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-the-laravel-query-builder-to-write-a-query-in-php)