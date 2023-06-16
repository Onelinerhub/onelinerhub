# How do I use Laravel Keyby in PHP?
// plain

To use Laravel Keyby in PHP, you must first install the Keyby package using Composer.
```
composer require laravel/keyby
```

Once the package is installed, you can use the Keyby facade to access the keyby() helper. This helper allows you to access an array of values using a key.

For example, if you have an array of users with their corresponding IDs, you can use the keyby() helper to access a particular user by their ID:

```
$users = [
    [
        'id' => 1,
        'name' => 'John Doe',
    ],
    [
        'id' => 2,
        'name' => 'Jane Doe',
    ],
];

$user = keyby($users, 'id', 2);

echo $user['name']; // Outputs "Jane Doe"
```

The keyby() helper takes three arguments: the array to be searched, the key to search by, and the value to search for. It then returns the first element in the array that matches the given key and value.

You can also use the keyby() helper to search for multiple elements at once. To do this, pass an array of values as the third argument.

```
$users = [
    [
        'id' => 1,
        'name' => 'John Doe',
    ],
    [
        'id' => 2,
        'name' => 'Jane Doe',
    ],
    [
        'id' => 3,
        'name' => 'Foo Bar',
    ],
];

$users = keyby($users, 'id', [1, 3]);

print_r($users);

/* Outputs
Array
(
    [0] => Array
        (
            [id] => 1
            [name] => John Doe
        )

    [1] => Array
        (
            [id] => 3
            [name] => Foo Bar
        )

)
*/
```

Laravel Keyby is a powerful and convenient way to access elements in an array using a key.

## Helpful links

- [Laravel Keyby Documentation](https://laravel.com/docs/master/keyby)
- [GitHub Repository](https://github.com/laravel/keyby)

onelinerhub: [How do I use Laravel Keyby in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-keyby-in-php)