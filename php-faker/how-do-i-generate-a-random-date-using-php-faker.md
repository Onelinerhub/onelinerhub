# How do I generate a random date using PHP Faker?
// plain

The easiest way to generate a random date using PHP Faker is to use the `dateTime()` method. It generates a random dateTime object based on the passed parameters.

## Example code

```
$faker = Faker\Factory::create();
$randomDate = $faker->dateTime;
```

## Output example

```
DateTime Object
(
    [date] => 2020-05-27 23:20:59.000000
    [timezone_type] => 3
    [timezone] => UTC
)
```

## Code explanation

- `Faker\Factory::create()` - creates and returns a new Faker\Generator instance.
- `dateTime()` - generates a random dateTime object.
- `$randomDate` - stores the generated dateTime object.

## Helpful links
- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderdatetime)

onelinerhub: [How do I generate a random date using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-date-using-php-faker)