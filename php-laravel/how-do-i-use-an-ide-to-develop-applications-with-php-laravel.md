# How do I use an IDE to develop applications with PHP Laravel?
// plain

Using an IDE to develop applications with PHP Laravel is quite simple. First, install a suitable IDE such as [Visual Studio Code](https://code.visualstudio.com/). Then, install the Laravel extension for the IDE. This will provide support for syntax highlighting, autocomplete, and other features.

Next, create a new project with the `laravel new` command. This will create the necessary files and directories for the project.

Once the project is created, you can start writing your application code. For example, here is a simple route that displays a welcome message:

```php
Route::get('/', function () {
    return view('welcome');
});
```

The IDE can provide helpful features such as code completion and syntax highlighting. This makes it easier to write and understand code.

Finally, you can run the application with the `php artisan serve` command. This will start a local server and you can view the application in your browser.

## Helpful links

- [Laravel Documentation](https://laravel.com/docs/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Laravel Extension](https://marketplace.visualstudio.com/items?itemName=onecentlin.laravel-extension-pack)

onelinerhub: [How do I use an IDE to develop applications with PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-use-an-ide-to-develop-applications-with-php-laravel)