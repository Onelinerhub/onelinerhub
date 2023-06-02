# How do I generate a fake year in Laravel using Faker?
// plain

To generate a fake year in Laravel using Faker, you can use the `year` method provided by Faker. It will generate a random year between the current year and 100 years ago.

## Example code

```php
$faker = Faker\Factory::create();
$year = $faker->year;
echo $year;
```

## Output example

```
1958
```

The code above creates a Faker instance and then calls the `year` method to generate a random year between the current year and 100 years ago. The output of the code in the example is `1958`.

The code consists of the following parts:

1. `$faker = Faker\Factory::create();` - creates a Faker instance.
2. `$year = $faker->year;` - calls the `year` method on the Faker instance.
3. `echo $year;` - prints the generated year.

## Helpful links

- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderdatetimeyear)

onelinerhub: [How do I generate a fake year in Laravel using Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-fake-year-in-laravel-using-faker)