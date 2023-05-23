# How to sort a collection in Symfony with PHP?
// plain

Sorting a collection in Symfony with PHP can be done using the `usort()` function. This function takes two parameters: a callback function and the array to be sorted. The callback function should take two parameters and return an integer.

## Example code

```php
$collection = [
    ['name' => 'John', 'age' => 20],
    ['name' => 'Jane', 'age' => 25],
    ['name' => 'Bob', 'age' => 15],
];

usort($collection, function($a, $b) {
    return $a['age'] <=> $b['age'];
});
```

## Output example

```
Array
(
    [0] => Array
        (
            [name] => Bob
            [age] => 15
        )

    [1] => Array
        (
            [name] => John
            [age] => 20
        )

    [2] => Array
        (
            [name] => Jane
            [age] => 25
        )

)
```

## Code explanation

- `usort()`: This is the function used to sort the collection. It takes two parameters: a callback function and the array to be sorted.
- `$a` and `$b`: These are the two parameters passed to the callback function. They represent two elements of the array to be compared.
- `$a['age'] <=> $b['age']`: This is the comparison that is done between the two elements. The `<=>` operator returns -1, 0, or 1 depending on the result of the comparison.

## Helpful links
- [PHP usort() Function](https://www.w3schools.com/php/func_array_usort.asp)
- [PHP Spaceship Operator](https://www.php.net/manual/en/language.operators.comparison.php#language.operators.comparison.spaceship)

onelinerhub: [How to sort a collection in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-sort-a-collection-in-symfony-with-php)