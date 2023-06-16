# How can I create a tutorial using PHP and Laravel?
// plain

Creating a tutorial using PHP and Laravel is a relatively straightforward process.

First, create a new Laravel project with the command `composer create-project --prefer-dist laravel/laravel tutorial`.

Next, create a new controller with the command `php artisan make:controller TutorialController`. This will create a new controller class in the `app/Http/Controllers/TutorialController.php` file.

In the controller file, add the following example code:

```php
public function index()
{
    return view('tutorial.index');
}
```

This code will create a new route, `tutorial.index`, that will render the view file `resources/views/tutorial/index.blade.php` when called.

Next, create a new view file in `resources/views/tutorial/index.blade.php` and add the following example code:

```html
<h1>Tutorial</h1>

<p>This is a tutorial.</p>
```

Finally, add the route to `routes/web.php` with the following code:

```php
Route::get('tutorial', 'TutorialController@index');
```

This will create a new route at `/tutorial` which will render the tutorial view file.

## Helpful links
- [Laravel Documentation](https://laravel.com/docs)
- [Laravel Routing Documentation](https://laravel.com/docs/7.x/routing)
- [Laravel Controllers Documentation](https://laravel.com/docs/7.x/controllers)

onelinerhub: [How can I create a tutorial using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-can-i-create-a-tutorial-using-php-and-laravel)