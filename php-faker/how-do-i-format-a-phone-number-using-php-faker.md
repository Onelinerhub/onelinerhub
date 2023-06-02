# How do I format a phone number using PHP Faker?
// plain

To format a phone number using PHP Faker, you can use the `$faker->phoneNumber` method. This method will return a random phone number in the format of `(###) ###-####`.

```
<?php

$faker = Faker\Factory::create();

$phoneNumber = $faker->phoneNumber;

echo $phoneNumber;

// Output: (819) 675-4337
?>
```

The code consists of three parts:
1. `$faker = Faker\Factory::create();` - This line instantiates a Faker object.
2. `$phoneNumber = $faker->phoneNumber;` - This line assigns a random phone number to the `$phoneNumber` variable.
3. `echo $phoneNumber;` - This line prints the phone number to the screen.

For more information on formatting phone numbers using PHP Faker, please refer to the [documentation](https://github.com/fzaninotto/Faker#formatters).

onelinerhub: [How do I format a phone number using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-format-a-phone-number-using-php-faker)