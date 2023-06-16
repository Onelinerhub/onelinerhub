# How do I create a controller in Laravel using PHP?
// plain

To create a controller in Laravel using PHP, you will need to use the artisan command line tool. The command to create a controller is `php artisan make:controller`. You can also specify the name of the controller, for example `php artisan make:controller MyController`.

```
$ php artisan make:controller MyController
Controller created successfully.
```

The command will create a controller file in the `app/Http/Controllers` directory. The content of the controller file will look like this:

```
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MyController extends Controller
{
    //
}
```

The controller class will extend the `Controller` class from the `Illuminate\Routing\Controller` namespace. You can add methods to the controller class to define the routes and logic for your application.

For more information about controllers in Laravel, please refer to the [Laravel Documentation](https://laravel.com/docs/7.x/controllers).

onelinerhub: [How do I create a controller in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-create-a-controller-in-laravel-using-php)