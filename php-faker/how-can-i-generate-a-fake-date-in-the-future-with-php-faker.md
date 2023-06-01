# How can I generate a fake date in the future with PHP Faker?
// plain

You can generate a fake date in the future with PHP Faker using the [`dateTimeBetween()`](https://github.com/fzaninotto/Faker#datetime) method. This method takes two parameters, the first being the start date and the second being the end date. Here is an example of generating a future date with PHP Faker:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$futureDate = $faker->dateTimeBetween('now', '+5 days');

echo $futureDate->format('Y-m-d H:i:s');

// Output: 2020-11-19 11:14:25
?>
```

The code above uses the `dateTimeBetween()` method to generate a future date between the current date and 5 days from now. The `dateTimeBetween()` method returns a `DateTime` object, so we must use the `format()` method to convert it to the desired format. In this case, we used the format `Y-m-d H:i:s` to output a date string in the format `2020-11-19 11:14:25`.

## Helpful links

- [Faker GitHub Repository](https://github.com/fzaninotto/Faker)
- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderdatetime)

onelinerhub: [How can I generate a fake date in the future with PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-date-in-the-future-with-php-faker)