# How do I create an admin panel in Laravel using PHP?
// plain

Creating an admin panel in Laravel using PHP is relatively simple. First, create a new controller for the admin panel. This controller should contain all the logic necessary to display the admin panel view.

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AdminController extends Controller
{
    public function index()
    {
        return view('admin.index');
    }
}
```

Next, create the corresponding view file to display the admin panel. This view file should contain all the HTML and other markup necessary to render the admin panel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Admin Panel</title>
    </head>
    <body>
        <h1>Admin Panel</h1>
    </body>
</html>
```

Finally, register the controller in the `routes/web.php` file.

```php
Route::get('/admin', 'AdminController@index');
```

Once these steps have been completed, the admin panel should be accessible at the `/admin` route.

## Code explanation


1. `AdminController` - A controller containing all the logic necessary to display the admin panel view.
2. `admin.index` - The view file containing the HTML and other markup necessary to render the admin panel.
3. `routes/web.php` - The file where the `AdminController` is registered.

## Helpful links

- [Laravel Documentation - Controllers](https://laravel.com/docs/7.x/controllers)
- [Laravel Documentation - Views](https://laravel.com/docs/7.x/views)
- [Laravel Documentation - Routing](https://laravel.com/docs/7.x/routing)

onelinerhub: [How do I create an admin panel in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-create-an-admin-panel-in-laravel-using-php)