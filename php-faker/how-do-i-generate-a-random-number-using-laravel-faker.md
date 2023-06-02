# How do I generate a random number using Laravel Faker?
// plain

Generating a random number using Laravel Faker is quite simple. All you need to do is use the `numberBetween` method. Here is an example of how to generate a random number between 1 and 10:

```
use Faker\Generator as Faker;

$faker = Faker::create();
$randomNumber = $faker->numberBetween(1, 10);
echo $randomNumber;
```

## Output example

```
8
```

The code above uses the `Faker` class to create an instance of the Faker generator, then uses the `numberBetween` method to generate a random number between the two parameters passed in. The output of the code above is a random number between 1 and 10.

## Code explanation


- `use Faker\Generator as Faker;` - This line imports the `Faker` class from the `Faker` namespace.

- `$faker = Faker::create();` - This line creates an instance of the Faker generator.

- `$randomNumber = $faker->numberBetween(1, 10);` - This line uses the `numberBetween` method from the `Faker` instance to generate a random number between the two parameters passed in.

- `echo $randomNumber;` - This line prints out the random number generated.

## Helpful links

- [Laravel Faker Documentation](https://laravel.com/docs/7.x/faker)

onelinerhub: [How do I generate a random number using Laravel Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-number-using-laravel-faker)