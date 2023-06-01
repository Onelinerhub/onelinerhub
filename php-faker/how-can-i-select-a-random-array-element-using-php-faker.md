# How can I select a random array element using PHP Faker?
// plain

Using the PHP Faker library, you can easily select a random array element with the `randomElement` method. Here is an example of how you could use it:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$array = array(
    'a',
    'b',
    'c',
    'd',
    'e'
);

echo $faker->randomElement($array);

// Output: e
```

The `randomElement` method takes an array as an argument and returns a random element from the array. In the example above, the output would be one of the five letters in the array, randomly selected.

## Code explanation


- `require_once 'vendor/autoload.php';` - This is used to include the autoloader file from the Faker library.
- `$faker = Faker\Factory::create();` - This is used to create a new Faker instance.
- `$array = array(...)` - This is used to create an array with five elements.
- `echo $faker->randomElement($array);` - This is used to select a random element from the array and print it to the screen.

## Helpful links

- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderbase)
- [PHP Faker API Reference](https://github.com/fzaninotto/Faker/blob/master/src/Faker/Provider/Base.php)

onelinerhub: [How can I select a random array element using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-select-a-random-array-element-using-php-faker)