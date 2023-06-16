# How do I create a controller in Laravel using PHP?
// plain

To create a controller in Laravel using PHP, you need to use the `artisan` command line utility.

First, create a controller class in the `app/Http/Controllers` directory:

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MyController extends Controller
{
    //
}
```

Next, generate the controller using the `artisan` command:
```
php artisan make:controller MyController
```

This will create the controller file and add the following code to it:
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MyController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
```

The controller class contains 8 methods: `index`, `create`, `store`, `show`, `edit`, `update`, `destroy`.

Each of these methods is responsible for performing a specific action, like displaying a form, creating a resource, or deleting a resource.

You can add your own custom logic to these methods to create the desired functionality.

## Helpful links

- [Laravel Documentation - Controllers](https://laravel.com/docs/7.x/controllers)
- [Laravel Artisan Command Line Utility](https://laravel.com/docs/7.x/artisan)

onelinerhub: [How do I create a controller in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-create-a-controller-in-laravel-using-php-1686943264)