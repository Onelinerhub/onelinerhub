# How do I create a basic example using PHP and Laravel?
// plain

To create a basic example using PHP and Laravel, you will need to have a basic understanding of both languages. The example below will demonstrate how to create a route, controller, and view for a basic web page.

```
// routes/web.php

Route::get('/', 'HomeController@index');

// app/Http/Controllers/HomeController.php

<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    public function index()
    {
        return view('home');
    }
}

// resources/views/home.blade.php

<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to the Home Page!</h1>
    </body>
</html>
```

The code above creates a route for the home page, a controller for the home page, and a view for the home page. The route will point to the controller, which will then return the view. When the page is accessed, the view will be rendered and the output will be:

```
<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to the Home Page!</h1>
    </body>
</html>
```

For more information on how to use PHP and Laravel together, please see the following links:

- [Laravel Documentation](https://laravel.com/docs)
- [PHP Documentation](https://www.php.net/docs.php)

onelinerhub: [How do I create a basic example using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-create-a-basic-example-using-php-and-laravel)