# How do I generate a random date between two dates using PHP Faker?
// plain

Using PHP Faker you can generate a random date between two dates by calling the `dateTimeBetween` method. This method requires two parameters: the start and end date. The example code below will generate a random date in between two dates:

```
$faker = Faker\Factory::create();
$randomDate = $faker->dateTimeBetween('-30 years', 'now');
echo $randomDate->format('Y-m-d H:i:s');
```

## Output example

```
1994-07-31 21:30:54
```

The code above creates a new Faker instance and uses the `dateTimeBetween` method to generate a random date in between two dates. The two parameters `'-30 years'` and `'now'` specify the start and end date respectively. The `format` method is used to format the date in the desired format.

Parts of the code:
- `$faker = Faker\Factory::create();`: Creates a new Faker instance.
- `$randomDate = $faker->dateTimeBetween('-30 years', 'now');`: Generates a random date in between two dates.
- `echo $randomDate->format('Y-m-d H:i:s');`: Formats the date in the desired format.

## Helpful links
- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderdatetime)

onelinerhub: [How do I generate a random date between two dates using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-date-between-two-dates-using-php-faker)