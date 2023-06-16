# How can I get request parameters in my Laravel application using PHP?
// plain

The most common way to get request parameters in a Laravel application using PHP is to use the `Input` facade. The `Input` facade provides an easy way to access user input from the request. For example:

```php
$name = Input::get('name');
echo $name;
```

The above code will output the value of the `name` request parameter.

The `Input` facade provides a few more methods for accessing request parameters. These include:

* `Input::all()` - Returns an array of all request parameters
* `Input::only()` - Returns an array containing only the specified parameters
* `Input::except()` - Returns an array of all request parameters except for the specified parameters
* `Input::has()` - Returns true if the request contains the specified parameter

For more information, see the [Laravel documentation on Input](https://laravel.com/docs/5.7/requests#retrieving-input).

onelinerhub: [How can I get request parameters in my Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-can-i-get-request-parameters-in-my-laravel-application-using-php)