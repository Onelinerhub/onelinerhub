# How do I use a template in Laravel with PHP?
// plain

Using a template in Laravel with PHP is a simple process. The first step is to create a view file, which will contain the HTML for the template. This view file should be placed in the `/resources/views` directory.

Next, create a route in the `routes/web.php` file that points to the view file. For example, to show the view file `example.blade.php`:

```
Route::get('example', function () {
    return view('example');
});
```

The view file can contain plain HTML as well as Blade syntax, which allows for dynamic content to be included. Blade syntax is denoted using double curly braces. For example, to include a variable called `$name`:

```
<h1>Hello, {{ $name }}</h1>
```

Blade also allows for the inclusion of partials, which are reusable components. To include a partial, use the `@include` directive and pass the name of the file as a parameter:

```
@include('partials.header')
```

Finally, the view can be passed data from the controller. This is done by passing an array as the second parameter of the `view()` method. For example, to pass the variable `$name`:

```
return view('example', ['name' => $name]);
```

For more information on using templates in Laravel, see the [Laravel documentation](https://laravel.com/docs/7.x/blade).

#### List of Code Parts with Explanation

1. `Route::get('example', function () { return view('example'); });` - This line of code creates a route for the view file `example.blade.php`.

2. `<h1>Hello, {{ $name }}</h1>` - This line of code uses Blade syntax to include a variable called `$name` in the view file.

3. `@include('partials.header')` - This line of code uses the `@include` directive to include a partial called `partials.header`.

4. `return view('example', ['name' => $name]);` - This line of code passes a variable called `$name` to the view file.

onelinerhub: [How do I use a template in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-a-template-in-laravel-with-php)