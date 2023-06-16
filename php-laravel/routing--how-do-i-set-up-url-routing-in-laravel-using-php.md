# routing

How do I set up URL routing in Laravel using PHP?
// plain

URL routing in Laravel is a way of mapping a URL to a specific action in a controller. It allows you to create custom routes that are meaningful and easy to remember for visitors to your site.

To set up URL routing in Laravel using PHP, you need to use the route() function. This function takes two arguments: the URL path and the action that should be triggered when the URL is visited.

For example, the following code will map the URL `/example` to the `ExampleController@exampleAction` action:
```
Route::get('/example', 'ExampleController@exampleAction');
```

The first argument is the URL path, which can be a string or a regular expression. The second argument is the action that should be triggered when the URL is visited. This can be a closure, a controller action, or a named route.

In addition to the route() function, you can also use the group() function to group related routes together. This can be useful for organizing your routes and making them easier to maintain.

The following code will group all routes related to the `ExampleController` controller:
```
Route::group(['prefix' => 'example'], function () {
    Route::get('/', 'ExampleController@indexAction');
    Route::get('/{id}', 'ExampleController@showAction');
    Route::post('/', 'ExampleController@storeAction');
});
```

The group() function takes two arguments: an array of options and a closure. The closure contains the routes that should be grouped together.

## Helpful links
- [Laravel Routing Documentation](https://laravel.com/docs/master/routing)
- [PHP Route Function](https://www.php.net/manual/en/function.route.php)

onelinerhub: [routing

How do I set up URL routing in Laravel using PHP?](https://onelinerhub.com/php-laravel/routing--how-do-i-set-up-url-routing-in-laravel-using-php)