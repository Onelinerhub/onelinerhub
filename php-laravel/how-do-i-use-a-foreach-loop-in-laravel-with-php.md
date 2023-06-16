# How do I use a foreach loop in Laravel with PHP?
// plain

A `foreach` loop is a common type of loop used in PHP and Laravel. It is used to iterate through each item in an array or collection. Here is an example of how to use it in Laravel with PHP:

```
$items = [
    'item1',
    'item2',
    'item3'
];

foreach ($items as $item) {
    echo $item;
}
```

This code will output `item1item2item3`.

The `foreach` loop consists of three parts:
1. The array or collection to loop through (`$items` in this example).
2. The `foreach` keyword.
3. The loop body (`echo $item;` in this example).

The `foreach` keyword takes two parameters: the array or collection and a variable to represent each item in the array or collection. In the example, `$item` is the variable that represents each item in the `$items` array.

For more information, see the [PHP documentation](https://www.php.net/manual/en/control-structures.foreach.php) and the [Laravel documentation](https://laravel.com/docs/7.x/collections#method-each).

onelinerhub: [How do I use a foreach loop in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-a-foreach-loop-in-laravel-with-php)