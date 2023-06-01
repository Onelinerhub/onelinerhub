# How can I generate gender-specific data with Laravel Faker?
// plain

Generating gender-specific data with Laravel Faker is easy. It can be done with the `randomElement` method, which takes an array of elements and returns a random one. Here is an example code block with an example output:

```
$faker = Faker\Factory::create();
$gender = $faker->randomElement(['male', 'female']);
echo $gender;
```

## Output example

```
male
```

The code above creates a Faker instance and then uses `randomElement` to get a random gender from the array of `male` and `female`.

## Code explanation


- `$faker = Faker\Factory::create();` - This creates a new Faker instance.

- `$gender = $faker->randomElement(['male', 'female']);` - This uses the `randomElement` method to get a random gender from the array of `male` and `female`.

- `echo $gender;` - This prints the randomly selected gender.

## Helpful links
- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#formatters)
- [Faker randomElement](https://github.com/fzaninotto/Faker#randomelement)

onelinerhub: [How can I generate gender-specific data with Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-gender-specific-data-with-laravel-faker)