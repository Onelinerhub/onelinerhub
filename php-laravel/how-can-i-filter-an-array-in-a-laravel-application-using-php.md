# How can I filter an array in a Laravel application using PHP?
// plain

In order to filter an array in a Laravel application using PHP, you can use the `array_filter` function. This function takes a callback function as its first argument, which is used to determine whether a value should be included in the resulting array or not.

```php
$array = [1, 2, 3, 4, 5];

$filteredArray = array_filter($array, function ($value) {
    return $value % 2 === 0;
});

print_r($filteredArray);
```

## Output example

```
Array
(
    [1] => 2
    [3] => 4
)
```

The code above filters out all odd numbers from the `$array` and stores the resulting array in the `$filteredArray` variable. The callback function checks each element of the array to see if it is divisible by 2 (`$value % 2 === 0`) and returns `true` if it is, or `false` otherwise.

The `array_filter` function can also be used to filter an associative array, where the key-value pairs are preserved.

```php
$assocArray = [
    'a' => 1,
    'b' => 2,
    'c' => 3,
    'd' => 4,
    'e' => 5
];

$filteredAssocArray = array_filter($assocArray, function ($value) {
    return $value % 2 === 0;
});

print_r($filteredAssocArray);
```

## Output example

```
Array
(
    [b] => 2
    [d] => 4
)
```

The code above filters out all odd numbers from the `$assocArray` and stores the resulting array in the `$filteredAssocArray` variable.

## Helpful links
- [PHP array_filter() Function](https://www.w3schools.com/php/func_array_filter.asp)
- [Laravel Arrays & Objects](https://laravel.com/docs/7.x/collections)

onelinerhub: [How can I filter an array in a Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-can-i-filter-an-array-in-a-laravel-application-using-php)