# How can I use Laravel helpers in my PHP project?
// plain

You can use Laravel helpers in your PHP project by calling the `helper()` method on the `Illuminate\Support\Facades\Facade` class. This method takes a string parameter which is the name of the helper function you wish to use.

For example, to use the `str_slug()` helper, you can do the following:
```
use Illuminate\Support\Facades\Facade;

$slug = Facade::helper('str_slug')('My Slug');
echo $slug;
```

This will output `my-slug`.

You can also use the `helper()` method to access other helper functions, such as `array_get()` and `data_get()`.

Here's an example of how to use the `array_get()` helper:
```
use Illuminate\Support\Facades\Facade;

$array = [
    'foo' => 'bar',
    'baz' => 'qux'
];

$value = Facade::helper('array_get')($array, 'foo');
echo $value;
```

This will output `bar`.

For more information on Laravel helpers, you can refer to the [official documentation](https://laravel.com/docs/7.x/helpers).

onelinerhub: [How can I use Laravel helpers in my PHP project?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-helpers-in-my-php-project)