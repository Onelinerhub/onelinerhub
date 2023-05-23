# How to convert an object to an array in PHP Symfony?
// plain

Objects in PHP Symfony can be converted to arrays using the `get_object_vars()` function. This function takes an object as an argument and returns an array containing all of the object's properties.

## Example code

```
$object = new stdClass();
$object->name = 'John';
$object->age = 25;

$array = get_object_vars($object);
```

## Output example

```
Array
(
    [name] => John
    [age] => 25
)
```

## Code explanation

- `$object`: This is the object that will be converted to an array.
- `get_object_vars()`: This is the function that takes an object as an argument and returns an array containing all of the object's properties.
- `$array`: This is the array that will contain the object's properties.

## Helpful links
- [PHP get_object_vars() Function](https://www.w3schools.com/php/func_misc_get_object_vars.asp)

onelinerhub: [How to convert an object to an array in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-convert-an-object-to-an-array-in-php-symfony)