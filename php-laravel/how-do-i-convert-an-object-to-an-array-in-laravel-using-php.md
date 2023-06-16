# How do I convert an object to an array in Laravel using PHP?
// plain

The easiest way to convert an object to an array in Laravel using PHP is to use the `toArray()` method. This method will return an array representation of the object.

## Example code

```
$user = User::find(1);
$userArray = $user->toArray();
```

The `$userArray` variable will contain an array representation of the object.

The `toArray()` method will return an array with the object's public properties and their values. It will also include any `App\Model` relationships.

The following list contains the parts of the code and their explanation:
- `$user`: this is a `User` object returned from the `find()` method.
- `$userArray`: this is an array representation of the `$user` object.
- `toArray()`: this is the method that will convert the object to an array.

## Helpful links
- [Laravel Documentation - Eloquent: Collections](https://laravel.com/docs/7.x/eloquent-collections#method-toarray)

onelinerhub: [How do I convert an object to an array in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-convert-an-object-to-an-array-in-laravel-using-php)