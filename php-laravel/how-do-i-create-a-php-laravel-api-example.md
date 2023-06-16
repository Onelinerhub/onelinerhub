# How do I create a PHP Laravel API example?
// plain

Creating a PHP Laravel API example is fairly straightforward. First, create a Laravel project using the `laravel new` command:

```
laravel new my-project
```

This will create a new project in the `my-project` directory.

Next, create a controller in the `app/Http/Controllers` directory. This controller will handle the API requests. For example:

```
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ApiController extends Controller
{
    public function index()
    {
        return response()->json([
            'message' => 'Hello World!'
        ]);
    }
}
```

This controller will return a JSON response with the message "Hello World!".

Finally, create a route in the `routes/web.php` file to map the URL to the controller:

```
Route::get('/api', 'ApiController@index');
```

Now when you visit the `/api` URL, you will get the JSON response.

## Helpful links

- [Laravel Documentation](https://laravel.com/docs)
- [Laravel Routes](https://laravel.com/docs/7.x/routing)
- [Laravel Controllers](https://laravel.com/docs/7.x/controllers)

onelinerhub: [How do I create a PHP Laravel API example?](https://onelinerhub.com/php-laravel/how-do-i-create-a-php-laravel-api-example)