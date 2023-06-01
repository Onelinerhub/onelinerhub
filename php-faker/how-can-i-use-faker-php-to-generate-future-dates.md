# How can I use Faker PHP to generate future dates?
// plain

Faker PHP is a great tool for generating fake data, including dates. To generate a future date using Faker PHP, you can use the `dateTimeBetween()` method. This method takes two parameters: a start date and an end date. The start date should be the current date, and the end date should be the desired future date.

## Example code


```
$faker = Faker\Factory::create();
$futureDate = $faker->dateTimeBetween('now', '+5 days');
echo $futureDate->format('Y-m-d H:i:s');
```

## Output example

```
2020-05-27 19:09:33
```

This example code generates a future date that is 5 days from the current date. This code does the following:

1. Creates a Faker\Factory instance, which provides access to all Faker methods.
2. Calls `dateTimeBetween()` with two parameters: `now`, which is the current date, and `+5 days`, which is the desired future date.
3. Formats the date using the `format()` method.

For more information about Faker PHP and generating dates, see the following links:

- [Faker PHP Documentation](https://github.com/fzaninotto/Faker#formatters)
- [Generating Dates with Faker PHP](https://github.com/fzaninotto/Faker#date-and-time)

onelinerhub: [How can I use Faker PHP to generate future dates?](https://onelinerhub.com/php-faker/how-can-i-use-faker-php-to-generate-future-dates)