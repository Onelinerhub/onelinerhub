# How can I generate unique data with Laravel Faker?
// plain

You can generate unique data with Laravel Faker by using the unique() method. This method will generate a random unique value each time it is called.

For example:

```
$uniqueNumber = \Faker\Factory::create()->unique()->numberBetween($min = 1, $max = 9999);
echo $uniqueNumber;
```

## Output example

```
5577
```

The code above will generate a random number between 1 and 9999.

The parts of the code are:
- \Faker\Factory::create() - creates a new Faker\Generator instance
- unique() - the method used to generate a unique value
- numberBetween($min = 1, $max = 9999) - generates a random number between 1 and 9999

For more information about Laravel Faker, please refer to the [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovidernumber).

onelinerhub: [How can I generate unique data with Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-unique-data-with-laravel-faker)