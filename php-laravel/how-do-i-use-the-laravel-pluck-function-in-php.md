# How do I use the Laravel Pluck function in PHP?
// plain

The Laravel Pluck function is a powerful tool for extracting values from collections. It allows you to select specific values from a collection of objects or arrays.

For example, you can use Pluck to retrieve the names of all users in a collection:

```
$userNames = User::all()->pluck('name');
```

The output of the above code will be a collection of strings, each representing the name of a user:

```
[
    'John',
    'Jane',
    'Jack',
    'Jill'
]
```

The Pluck function takes two arguments, the first being the key of the value to be extracted, and the second being an optional callback function used to manipulate the result.

For example, if you wanted to get the names of all users in uppercase:

```
$userNames = User::all()->pluck('name', function($name) {
    return strtoupper($name);
});
```

The output of the above code will be a collection of strings, each representing the name of a user in uppercase:

```
[
    'JOHN',
    'JANE',
    'JACK',
    'JILL'
]
```

You can find more information about the Laravel Pluck function in the official [Laravel documentation](https://laravel.com/docs/7.x/collections#method-pluck).

onelinerhub: [How do I use the Laravel Pluck function in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-pluck-function-in-php)