# How can I use an array in Laravel with PHP?
// plain

An array is a data structure that stores multiple values in a single variable. In Laravel with PHP, you can use an array to store and manipulate data. Here is an example of how to use an array in Laravel with PHP:

```
$data = array(
    'name' => 'John',
    'age' => 25,
    'location' => 'New York'
);

echo $data['name'];
// Output: John
```

The code above creates an array called `$data` with three elements, each of which is a key-value pair. The keys are `name`, `age`, and `location`, and the values are `John`, `25`, and `New York`, respectively. To access a value from the array, you can use the key in square brackets after the array name. In this example, `echo $data['name']` returns the value `John`.

## Code explanation


- `$data`: This is the name of the array.
- `array()`: This is the PHP function used to create an array.
- `'name' => 'John'`: These are the key-value pairs that make up the array. The key is `name` and the value is `John`.
- `echo $data['name']`: This is how you access the value of a key in the array. In this example, it returns the value `John`.

Here are some relevant links for more information:

- [PHP Arrays](https://www.w3schools.com/php/php_arrays.asp)
- [Laravel Arrays](https://laravel.com/docs/5.8/arrays)

onelinerhub: [How can I use an array in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-an-array-in-laravel-with-php)