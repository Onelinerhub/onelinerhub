# How do I convert an array to an object in PHP Laravel?
// plain

To convert an array to an object in PHP Laravel, you can use the `collect()` helper method. This method takes an array and returns an instance of the `Illuminate\Support\Collection` class.

## Example code

```
$array = [
    'name' => 'John Doe',
    'age' => 32
];

$object = collect($array);
```

The `collect()` helper method can also be used to convert an object to an array.

## Example code

```
$object = new stdClass();
$object->name = 'John Doe';
$object->age = 32;

$array = collect($object)->toArray();
```
## Output example

```
Array
(
    [name] => John Doe
    [age] => 32
)
```

The `collect()` helper method is part of the [Laravel Collection](https://laravel.com/docs/7.x/collections) class. It provides a variety of methods for manipulating and transforming arrays and objects.

## Helpful links
- [Laravel Collection](https://laravel.com/docs/7.x/collections)
- [PHP Arrays](https://www.php.net/manual/en/language.types.array.php)
- [PHP Objects](https://www.php.net/manual/en/language.types.object.php)

onelinerhub: [How do I convert an array to an object in PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-convert-an-array-to-an-object-in-php-laravel)