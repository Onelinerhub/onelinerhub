# How do I use PHP Laravel Blade to create a dynamic website?
// plain

Using PHP Laravel Blade to create a dynamic website is very simple and straightforward. Here is an example code block to demonstrate how to use Blade to create a dynamic website:

```
// Create a Route
Route::get('/', function () {
    // Create a view
    return view('home');
});

// Create a View
@extends('layout')

@section('content')
    <h1>Welcome to my website!</h1>
    <p>This is a dynamic website created using PHP Laravel Blade.</p>
@endsection
```

In the example above, we have created a route and a view. The route is responsible for directing the user to the view. The view is responsible for the content that will be displayed on the webpage. The content in this example is a welcome message and a statement that the website is dynamic.

## Code explanation


1. `Route::get('/', function () {` - This is the route, which is responsible for directing the user to the view.
2. `return view('home');` - This line is responsible for telling the route which view to direct the user to. In this example, the view is called `home`.
3. `@extends('layout')` - This line is responsible for telling the view which layout to use.
4. `@section('content')` - This line is responsible for telling the view which section to use for the content.
5. `<h1>Welcome to my website!</h1>` - This is the content that will be displayed on the webpage.
6. `<p>This is a dynamic website created using PHP Laravel Blade.</p>` - This is the content that will be displayed on the webpage.
7. `@endsection` - This line is responsible for telling the view when the content section ends.

## Helpful links

- [Laravel Documentation - Blade](https://laravel.com/docs/7.x/blade)
- [Laravel Tutorial - Blade Templating](https://laracasts.com/series/laravel-from-scratch-2018/episodes/7)

onelinerhub: [How do I use PHP Laravel Blade to create a dynamic website?](https://onelinerhub.com/php-laravel/how-do-i-use-php-laravel-blade-to-create-a-dynamic-website)