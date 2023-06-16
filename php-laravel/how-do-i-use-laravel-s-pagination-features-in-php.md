# How do I use Laravel's pagination features in PHP?
// plain

Using Laravel's pagination features in PHP is easy. To get started, you must first install the Laravel pagination library. To do this, run the following command in your terminal:

```
composer require laravel/ui
```

Once you have installed the library, you can use the `paginate()` method in your controller to paginate the results of a query. For example, the following code will paginate the results of a query for all users in a database:

```
$users = User::paginate(10);
```

The `paginate()` method will return a `LengthAwarePaginator` instance, which can be used to generate the HTML for the pagination links. You can use the `links()` method to generate the HTML for the pagination links:

```
{{ $users->links() }}
```

This will generate HTML similar to the following:

```
<div>
    <span class="page-links">
        <a href="/users?page=1">1</a>
        <a href="/users?page=2">2</a>
        <a href="/users?page=3">3</a>
        ...
    </span>
</div>
```

You can also customize the pagination links using the `paginator()` method. It accepts an array of options that you can use to customize the pagination links. For more information, see the [Laravel Pagination Documentation](https://laravel.com/docs/7.x/pagination).

onelinerhub: [How do I use Laravel's pagination features in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-s-pagination-features-in-php)